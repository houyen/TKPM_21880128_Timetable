from django.db import models

# Create your models here.

import uuid

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from djchoices import DjangoChoices, ChoiceItem

from schools.models import School, Teacher
from utils.futils import get_current_admission_year
from utils.model_templates import LogicalDeleteModel, BaseModel


def validate_teacher_has_no_other_period(self):
    teacher_id = self.subject_teacher.teacher
    subject_teachers = SubjectTeacher.objects.filter(teacher=teacher_id)
    if (
        Period.objects.filter(
            weekday=self.weekday,
            period_number=self.period_number,
            subject_teacher__in=subject_teachers,
            admission_year=self.admission_year,
        )
        .exclude(pk=self.pk)
        .exists()
    ):
        period = Period.objects.get(
            weekday=self.weekday,
            period_number=self.period_number,
            subject_teacher__in=subject_teachers,
            admission_year=self.admission_year,
        )
        raise ValidationError(f"Teacher already has a period {period.id}")


def validate_same_school(self):
    if not self.subject_teacher.teacher.school == self.classroom.school:
        raise ValidationError(f"Teacher does not belongs to the same school")


class WeekDay(DjangoChoices):
    Monday = ChoiceItem(0)
    Tuesday = ChoiceItem(1)
    Wednesday = ChoiceItem(2)
    Thursday = ChoiceItem(3)
    Friday = ChoiceItem(4)
    Saturday = ChoiceItem(5)
    Sunday = ChoiceItem(6)


class ClassRoom(LogicalDeleteModel):
    standard = models.CharField(max_length=10)
    division = models.CharField(max_length=3)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.standard} {self.division}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['school', 'standard', "division"], name="unique_class_room")
        ]
        unique_together = ("standard", "division", "school")


class Subject(BaseModel):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.name


class SubjectTeacher(BaseModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.name}-{self.teacher.first_name}"


class Period(LogicalDeleteModel):
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    weekday = models.IntegerField(
        choices=WeekDay.choices, validators=[WeekDay.validator]
    )
    period_number = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)]
    )
    subject_teacher = models.ForeignKey(SubjectTeacher, on_delete=models.CASCADE)
    admission_year = models.IntegerField(default=get_current_admission_year)

    class Meta:
        unique_together = ("classroom", "weekday", "period_number", "admission_year")

    def clean(self, *args, **kwargs):
        validate_teacher_has_no_other_period(self)
        validate_same_school(self)
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class PeriodAdjustment(LogicalDeleteModel):
    adjusted_date = models.DateField()
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    adjusted_by = models.ForeignKey(SubjectTeacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("adjusted_date", "period")
