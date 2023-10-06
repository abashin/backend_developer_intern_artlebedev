from django.db import models
from django.utils import timezone


class Data(models.Model):
    fullName = models.CharField("Полное наименование", max_length=256)
    shortName = models.CharField("Сокращенное наименование", max_length=256, blank=True)
    address = models.CharField("Адрес", max_length=256, blank=True)
    ogrn = models.IntegerField("ОГРН/ОГРНИП", blank=True, default=0)
    licenseNumber = models.CharField("Номер лицензии", max_length=256, blank=True)
    licenseDate = models.DateTimeField("Дата регистрации лицензии")
    licenseStatus = models.BooleanField("Статус лицензии", default=False)
    pccDate = models.DateTimeField("Крайний срок первичного прохождения лицензиатами процедуры периодического подтверждения соответствия лицензионным требованиям", blank=True)

    inn = models.IntegerField("ИНН", blank=True, default=0)

    work1 = models.BooleanField("ОЛД_Разработка проектной документации по консервации, ремонту, реставрации, приспособлению и воссозданию объектов культурного наследия (памятников истории и культуры) народов Российской Федерации", default=False)
    work2 = models.BooleanField("ОЛД_Разработка проектной документации по инженерному укреплению объектов культурного наследия (памятников истории и культуры) народов Российской Федерации", default=False)
    work3 = models.BooleanField("ОЛД_Реставрация и воссоздание наружных и внутренних декоративно-художественных покрасок", default=False)
    work4 = models.BooleanField("ОЛД_Реставрация, консервация и воссоздание штукатурной отделки", default=False)
    work5 = models.BooleanField("ОЛД_Реставрация, консервация и воссоздание архитектурно-лепного декора", default=False)
    work6 = models.BooleanField("ОЛД_Реставрация, консервация и воссоздание поверхности из искусственного мрамора", default=False)
    work7 = models.BooleanField("ОЛД_Ремонт, реставрация и воссоздание кровель", default=False)
    work8 = models.BooleanField("ОЛД_Ремонт, реставрация и воссоздание металлических конструкций", default=False)
    work9 = models.BooleanField("ОЛД_Ремонт, реставрация и воссоздание оконных и дверных приборов", default=False)
    work10 = models.BooleanField("ОЛД_Ремонт, реставрация, консервация и воссоздание деревянных конструкций и деталей", default=False)
    work11 = models.BooleanField("ОЛД_Реставрация и воссоздание резьбы по деревянным конструкциям", default=False)
    work12 = models.BooleanField("ОЛД_Реставрация и воссоздание паркетных полов", default=False)
    work13 = models.BooleanField("ОЛД_Ремонт, реставрация и консервация ограждающих конструкций и распорных систем", default=False)
    work14 = models.BooleanField("ОЛД_Ремонт, реставрация, консервация и воссоздание оснований и фундаментов", default=False)
    work15 = models.BooleanField("ОЛД_Ремонт, реставрация, консервация и воссоздание кладок, конструкций", default=False)
    work16 = models.BooleanField("ОЛД_Реставрация, консервация и воссоздание мебели", default=False)
    work17 = models.BooleanField("ОЛД_Реставрация, консервация и воссоздание резьбы по дереву", default=False)
    work18 = models.BooleanField("ОЛД_Реставрация, воссоздание и консервация тканей, гобеленов и ковров", default=False)
    work19 = models.BooleanField("ОЛД_Реставрация и воссоздание осветительных приборов", default=False)
    work20 = models.BooleanField("ОЛД_Реставрация и воссоздание деталей из черного и цветных металлов", default=False)
    work21 = models.BooleanField("ОЛД_Реставрация и воссоздание позолоты", default=False)
    work22 = models.BooleanField("ОЛД_Реставрация и воссоздание керамического декора", default=False)
    work23 = models.BooleanField("ОЛД_Реставрация и воссоздание мозаики", default=False)
    work24 = models.BooleanField("ОЛД_Реставрация и воссоздание янтарного набора", default=False)
    work25 = models.BooleanField("ОЛД_Реставрация и воссоздание графики", default=False)
    work26 = models.BooleanField("ОЛД_Реставрация, консервация и воссоздание монументальной живописи", default=False)
    work27 = models.BooleanField("ОЛД_Реставрация, консервация и воссоздание станковой живописи", default=False)
    work28 = models.BooleanField("ОЛД_Реставрация, консервация и воссоздание скульптуры", default=False)
    work29 = models.BooleanField("ОЛД_Реставрация и воссоздание исторического ландшафта и произведений садово-паркового искусства", default=False)
    work30 = models.BooleanField("ОЛД_Приспособление инженерных систем и оборудования", default=False)
    work31 = models.BooleanField("ОЛД_Приспособление систем электрообеспечения", default=False)

    newWork1 = models.BooleanField("Разработка проектной документации по консервации, реставрации и воссозданию объектов культурного наследия (памятников истории и культуры) народов Российской Федерации", default=False)
    newWork2 = models.BooleanField("Разработка проектной документации по ремонту и приспособлению объектов культурного наследия (памятников истории и культуры) народов Российской Федерации", default=False)
    newWork3 = models.BooleanField("Реставрация, консервация и воссоздание оснований, фундаментов, кладок, ограждающих конструкций и распорных систем", default=False)
    newWork4 = models.BooleanField("Реставрация, консервация и воссоздание металлических конструкций и деталей", default=False)
    newWork5 = models.BooleanField("Реставрация, консервация и воссоздание деревянных конструкций и деталей", default=False)
    newWork6 = models.BooleanField("Реставрация, консервация и воссоздание декоративно-художественных покрасок, штукатурной отделки и архитектурно-лепного декора", default=False)
    newWork7 = models.BooleanField("Реставрация, консервация и воссоздание конструкций и деталей из естественного и искусственного камней", default=False)
    newWork8 = models.BooleanField("Реставрация, консервация и воссоздание произведений скульптуры и декоративно-прикладного искусства", default=False)
    newWork9 = models.BooleanField("Реставрация, консервация и воссоздание живописи (монументальной, станковой)", default=False)
    newWork10 = models.BooleanField("Реставрация, консервация и воссоздание исторического ландшафта и произведений садово-паркового искусства", default=False)
    newWork11 = models.BooleanField("Ремонт и приспособление объектов культурного наследия (памятников истории и культуры) народов Российской Федерации", default=False)

    orderNumber = models.IntegerField("Номер приказа о предоставлении лицензии", blank=True, default=0)

    orderDate = models.DateTimeField("Дата приказа")

    changeOrder = models.CharField("Номер приказа о переоформлении лицензии", max_length=256, blank=True)

    stoppingInfo = models.CharField("Основание", max_length=256, blank=True)

    terminationStatement = models.CharField("Основание прекращения действия лицензии", blank=True, max_length=256)

    terminationDate = models.DateTimeField("Дата прекращения действия лицензии", blank=True)

    inspectionsInfo = models.CharField("Основание проведения проверки", blank=True, max_length=512)

    penaltyInfo = models.DateTimeField("Дата постановления", blank=True)

    pathInfo = models.CharField("Сведения о первоисточнике записи", max_length=512)

    category = models.CharField("Категория объекта в исходной информационной системе", max_length=256)

    createDate = models.DateTimeField("Дата создания записи")

    updateDate = models.DateTimeField("Дата обновления записи")



    def __str__(self):
        return self.fullName

    class Meta:
        ordering = ['id']
        verbose_name = "Data"
        verbose_name_plural = "Data"