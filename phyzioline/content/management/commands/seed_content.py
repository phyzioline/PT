from django.core.management.base import BaseCommand

from content.models import EquivalenceRequirement, ExploreDataPoint


class Command(BaseCommand):
    help = 'Seed EquivalenceRequirement and ExploreDataPoint with sample data.'

    def handle(self, *args, **options):
        self.stdout.write('--- Seeding Equivalence Requirements Data ---')
        EquivalenceRequirement.objects.all().delete()

        countries_data = [
            {
                "ar_name": "المملكة العربية السعودية",
                "code": "SA",
                "reqs": "اجتياز اختبار الهيئة السعودية للتخصصات الصحية (SCFHS)، خبرة لا تقل عن سنتين بعد التخرج، تقييم الساعات السريرية.",
                "hours": "يتم تقييم الشهادة بناءً على برنامج جامعي 4-5 سنوات مع ما لا يقل عن 1000 ساعة تدريب سريري.",
                "exams": "اختبار البرومترك (Prometric) الإلزامي من SCFHS.",
                "notes": "الترخيص يتطلب التسجيل المهني وتصنيف الدرجة العلمية أولاً."
            },
            {
                "ar_name": "الولايات المتحدة الأمريكية",
                "code": "US",
                "reqs": "تقييم الشهادات الدراسية (Credential Evaluation) من FCCPT، شهادة التخرج وبيان الدرجات موثقة.",
                "hours": "يتطلب غالبًا الحصول على درجة (DPT) أو ما يعادلها. يتم مقارنة الساعات النظرية والعملية بدقة شديدة.",
                "exams": "اجتياز الامتحان الوطني للعلاج الطبيعي (NPTE) والحصول على ترخيص الولاية.",
                "notes": "متطلبات الترخيص تختلف من ولاية إلى أخرى (State Board)."
            },
            {
                "ar_name": "ألمانيا",
                "code": "DE",
                "reqs": "تقديم الأوراق لسلطة التكافؤ (Gleichwertigkeit).",
                "hours": "يتطلب حوالي 2900 ساعة نظري و 1600 ساعة عملي.",
                "exams": "امتحان المعرفة (Kenntnisprüfung).",
                "notes": "معرفة اللغة الألمانية (مستوى B2/C1) إلزامية."
            },
        ]

        for data in countries_data:
            EquivalenceRequirement.objects.create(
                country_name_ar=data['ar_name'],
                country_code=data['code'],
                official_requirements=data['reqs'],
                theoretical_practical_hours=data['hours'],
                mandatory_exams=data['exams'],
                general_notes=data.get('notes', '')
            )

        self.stdout.write(f"--- Successfully seeded {EquivalenceRequirement.objects.count()} Equivalence records. ---")

        # --- Explore data ---
        self.stdout.write('--- Seeding Explore Data Points ---')
        ExploreDataPoint.objects.all().delete()

        explore_data_points = [
            {"country": "المملكة العربية السعودية", "type": "THERAPISTS", "value": 15000, "year": 2024},
            {"country": "المملكة العربية السعودية", "type": "POPULATION", "value": 37000000, "year": 2024},
            {"country": "المملكة العربية السعودية", "type": "SCHOOLS", "value": 35, "year": 2024},
            {"country": "المملكة العربية السعودية", "type": "REHAB_CENTERS", "value": 450, "year": 2024},
            {"country": "الولايات المتحدة الأمريكية", "type": "THERAPISTS", "value": 350000, "year": 2024},
            {"country": "الولايات المتحدة الأمريكية", "type": "POPULATION", "value": 335000000, "year": 2024},
            {"country": "الولايات المتحدة الأمريكية", "type": "SCHOOLS", "value": 300, "year": 2024},
            {"country": "الولايات المتحدة الأمريكية", "type": "REHAB_CENTERS", "value": 15000, "year": 2024},
            {"country": "الإمارات العربية المتحدة", "type": "THERAPISTS", "value": 4000, "year": 2024},
            {"country": "الإمارات العربية المتحدة", "type": "POPULATION", "value": 10000000, "year": 2024},
            {"country": "الإمارات العربية المتحدة", "type": "SCHOOLS", "value": 8, "year": 2024},
            {"country": "الإمارات العربية المتحدة", "type": "REHAB_CENTERS", "value": 120, "year": 2024},
            {"country": "مصر", "type": "THERAPISTS", "value": 120000, "year": 2024},
            {"country": "مصر", "type": "POPULATION", "value": 115000000, "year": 2024},
            {"country": "مصر", "type": "SCHOOLS", "value": 40, "year": 2024},
            {"country": "مصر", "type": "REHAB_CENTERS", "value": 2000, "year": 2024},
            {"country": "ألمانيا", "type": "THERAPISTS", "value": 180000, "year": 2024},
            {"country": "ألمانيا", "type": "POPULATION", "value": 84000000, "year": 2024},
            {"country": "ألمانيا", "type": "SCHOOLS", "value": 400, "year": 2024},
            {"country": "ألمانيا", "type": "REHAB_CENTERS", "value": 8000, "year": 2024},
            {"country": "كندا", "type": "THERAPISTS", "value": 30000, "year": 2024},
            {"country": "كندا", "type": "POPULATION", "value": 41000000, "year": 2024},
            {"country": "كندا", "type": "SCHOOLS", "value": 25, "year": 2024},
            {"country": "كندا", "type": "REHAB_CENTERS", "value": 2000, "year": 2024},
        ]

        for d in explore_data_points:
            ExploreDataPoint.objects.create(
                country=d['country'],
                data_type=d['type'],
                value=d['value'],
                year=d['year']
            )

        self.stdout.write(f"--- Successfully seeded {ExploreDataPoint.objects.count()} Explore Data Points. ---")
