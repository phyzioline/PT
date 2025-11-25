"""
Utility script to load physiotherapy equivalency data inspired by the provided
`المعادلات بايثون.txt` file.

Usage:
    python load_equivalency_data.py
"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phyzioline_core.settings")
django.setup()

from equivalency.models import Country, EquivalencyRequirement, RequirementDocument

COUNTRY_EQUIVALENCY_DATA = {
    "USA": {
        "name_local": "الولايات المتحدة الأمريكية",
        "region": "North America",
        "continent": "americas",
        "summary": "يتطلب تقييم الشهادات واجتياز امتحان NPTE.",
        "studyHours": "قد تحتاج إلى مواد تكميلية للحصول على DPT أو ما يعادلها.",
        "accreditedHours": "يعتمد على تقرير هيئة التقييم مثل FCCPT.",
        "language": "TOEFL iBT بدرجة مرتفعة",
        "exam": "NPTE + Jurisprudence (حسب الولاية)",
        "documents": [
            "تقييم الشهادات من هيئة معتمدة مثل FCCPT",
            "شهادة التخرج وبيان الدرجات مترجمة وموثقة",
            "رخصة مزاولة المهنة المصرية",
            "شهادة إتقان اللغة الإنجليزية",
            "شهادة حسن سير وسلوك",
        ],
    },
    "UAE": {
        "name_local": "الإمارات العربية المتحدة",
        "region": "GCC",
        "continent": "asia",
        "summary": "يتطلب تقييم DataFlow واجتياز امتحان الجهة الصحية المختصة.",
        "studyHours": "يتم تقييم الشهادة عبر DataFlow.",
        "accreditedHours": "خبرة عملية موثقة لمدة سنتين على الأقل.",
        "language": "BLS ساري وامتحان الجهة (DHA/DOH/MOHAP)",
        "exam": "امتحان الهيئة الصحية + BLS",
        "documents": [
            "شهادة التخرج وبيان الدرجات مصدقة",
            "رخصة مزاولة المهنة المصرية",
            "شهادة خبرة سنتين",
            "شهادة حسن سير وسلوك",
            "تقرير DataFlow",
        ],
    },
    "KSA": {
        "name_local": "المملكة العربية السعودية",
        "region": "GCC",
        "continent": "asia",
        "summary": "التسجيل في الهيئة السعودية للتخصصات الصحية واجتياز Prometric.",
        "studyHours": "يتم التقييم عبر نظام ممارس بلس لتحديد التصنيف المهني.",
        "accreditedHours": "يعتمد على سنوات الخبرة بعد المؤهل.",
        "language": "BLS ساري",
        "exam": "Prometric + اختبارات الهيئة",
        "documents": [
            "شهادة التخرج وبيان الدرجات مصدقة",
            "رخصة مزاولة المهنة المصرية",
            "شهادة خبرة (يفضل سنتين)",
            "شهادة حسن سير وسلوك",
            "التسجيل في ممارس بلس",
        ],
    },
}


def main():
    for code, payload in COUNTRY_EQUIVALENCY_DATA.items():
        country, _ = Country.objects.get_or_create(
            code=code,
            defaults={
                "name_en": payload.get("name_local", code),
                "name_local": payload.get("name_local", ""),
                "region": payload.get("region", ""),
                "continent": payload.get("continent", "asia"),
            },
        )

        requirement, _ = EquivalencyRequirement.objects.get_or_create(
            country=country,
            summary=payload["summary"],
            defaults={
                "study_hours": payload.get("studyHours", ""),
                "accredited_hours": payload.get("accreditedHours", ""),
                "language_requirement": payload.get("language", ""),
                "exam_requirement": payload.get("exam", ""),
                "notes": "",
            },
        )

        for idx, doc in enumerate(payload.get("documents", []), start=1):
            RequirementDocument.objects.get_or_create(
                requirement=requirement,
                title=doc,
                defaults={"order": idx},
            )

    print("✅ Equivalency data loaded/updated successfully.")


if __name__ == "__main__":
    main()

