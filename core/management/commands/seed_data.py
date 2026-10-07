import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Village, Family, Member, Attendance


class Command(BaseCommand):
    help = "Seed database with initial data for ASHA Nurse dashboard"

    def handle(self, *args, **options):
        self.stdout.write("Seeding ASHA Care database...")

        # 1. Create Default User (Username: asha, PIN/Password: 123456)
        user, created = User.objects.get_or_create(username="asha")
        user.set_password("123456")
        user.email = "ashanurse@example.com"
        user.is_staff = True
        user.is_superuser = True
        user.first_name = "Sunita"
        user.last_name = "Sharma (ASHA Nurse)"
        user.save()
        if created:
            self.stdout.write(self.style.SUCCESS("Created default user 'asha' with PIN '123456'"))
        else:
            self.stdout.write(self.style.SUCCESS("Updated default user 'asha' with PIN '123456'"))

        # 2. Seed Villages
        v1, _ = Village.objects.get_or_create(
            village_number=101,
            defaults={"name": "Shanti Nagar (Sector A)", "total_houses": 120}
        )
        v2, _ = Village.objects.get_or_create(
            village_number=102,
            defaults={"name": "Kalyanpur Ward 4", "total_houses": 95}
        )
        v3, _ = Village.objects.get_or_create(
            village_number=103,
            defaults={"name": "Sundarpur Gram", "total_houses": 80}
        )
        self.stdout.write(self.style.SUCCESS("Villages verified."))

        # 3. Seed Families
        fam1, _ = Family.objects.get_or_create(
            village=v1,
            house_number=12,
            defaults={
                "family_name": "Sharma Parivar",
                "family_number": "FAM-101-012",
                "contact_number": "9876543210",
                "address": "Gali No. 3, Near Primary School, Shanti Nagar",
                "area": "Ward 2",
                "pin_code": "110085",
            }
        )

        fam2, _ = Family.objects.get_or_create(
            village=v1,
            house_number=24,
            defaults={
                "family_name": "Verma Family",
                "family_number": "FAM-101-024",
                "contact_number": "9812345678",
                "address": "House 24, Main Bazaar, Shanti Nagar",
                "area": "Ward 2",
                "pin_code": "110085",
            }
        )

        fam3, _ = Family.objects.get_or_create(
            village=v2,
            house_number=7,
            defaults={
                "family_name": "Yadav Parivar",
                "family_number": "FAM-102-007",
                "contact_number": "9723456789",
                "address": "Basti Road, Near Community Well, Kalyanpur",
                "area": "Kalyanpur East",
                "pin_code": "110086",
            }
        )

        fam4, _ = Family.objects.get_or_create(
            village=v3,
            house_number=15,
            defaults={
                "family_name": "Ansari Family",
                "family_number": "FAM-103-015",
                "contact_number": "9898765432",
                "address": "Panchayat Ghar Marg, Sundarpur Gram",
                "area": "Sundarpur",
                "pin_code": "110087",
            }
        )
        self.stdout.write(self.style.SUCCESS("Families verified."))

        # 4. Seed Members
        today = timezone.localdate()
        due_this_month = today.replace(day=min(25, today.day + 7 if today.day <= 21 else 28))
        due_next_month = (today + datetime.timedelta(days=45))

        # Sharma Parivar Members
        Member.objects.get_or_create(
            family=fam1,
            name="Ramesh Sharma",
            defaults={
                "gender": "Male",
                "blood_group": "B+",
                "relation": "Father",
                "date_of_birth": datetime.date(1982, 5, 14),
                "religion": "Hindu",
                "caste": "General",
                "bpl": False,
                "mobile_number": "9876543210",
                "aadhaar_number": "982345671234",
                "ayushman_card_number": "PMJAY-9823456712",
                "abha_number": "14-2345-6789-0123",
                "alive_status": "Alive",
                "remarks": "Hypertension under control. Regular checkup done.",
            }
        )

        # Pregnant Mother 1 (Due this month!)
        Member.objects.get_or_create(
            family=fam1,
            name="Pooja Sharma",
            defaults={
                "gender": "Female",
                "blood_group": "O+",
                "relation": "Mother",
                "date_of_birth": datetime.date(1996, 9, 20),
                "religion": "Hindu",
                "caste": "General",
                "bpl": False,
                "currently_pregnant": True,
                "pregnancy_start_date": today - datetime.timedelta(days=260),
                "expected_delivery_date": due_this_month,
                "mobile_number": "9876543211",
                "aadhaar_number": "982345671235",
                "ayushman_card_number": "PMJAY-9823456713",
                "abha_number": "14-2345-6789-0124",
                "alive_status": "Alive",
                "remarks": "3rd Trimester. IFA tablets supplied. Hospital delivery planned at Sub-District Hospital.",
            }
        )

        Member.objects.get_or_create(
            family=fam1,
            name="Aarav Sharma",
            defaults={
                "gender": "Male",
                "blood_group": "B+",
                "relation": "Son",
                "date_of_birth": datetime.date(2021, 3, 10),
                "religion": "Hindu",
                "caste": "General",
                "bpl": False,
                "mobile_number": "9876543210",
                "aadhaar_number": "982345671236",
                "ayushman_card_number": "PMJAY-9823456714",
                "abha_number": "14-2345-6789-0125",
                "alive_status": "Alive",
                "remarks": "All primary vaccinations up to age 3 completed.",
            }
        )

        # Verma Family Members
        # Pregnant Mother 2 (Due next month)
        Member.objects.get_or_create(
            family=fam2,
            name="Meena Verma",
            defaults={
                "gender": "Female",
                "blood_group": "A+",
                "relation": "Wife",
                "date_of_birth": datetime.date(1998, 11, 15),
                "religion": "Hindu",
                "caste": "OBC",
                "bpl": True,
                "bpl_number": "BPL-UP-2023-8874",
                "currently_pregnant": True,
                "pregnancy_start_date": today - datetime.timedelta(days=210),
                "expected_delivery_date": due_next_month,
                "mobile_number": "9812345678",
                "aadhaar_number": "543216789012",
                "ayushman_card_number": "PMJAY-5432167890",
                "abha_number": "",  # ABHA pending!
                "alive_status": "Alive",
                "remarks": "2nd ANC visit completed. Weight gain healthy.",
            }
        )

        Member.objects.get_or_create(
            family=fam2,
            name="Sunil Verma",
            defaults={
                "gender": "Male",
                "blood_group": "A+",
                "relation": "Husband",
                "date_of_birth": datetime.date(1994, 4, 18),
                "religion": "Hindu",
                "caste": "OBC",
                "bpl": True,
                "bpl_number": "BPL-UP-2023-8874",
                "mobile_number": "9812345678",
                "aadhaar_number": "543216789013",
                "ayushman_card_number": "",  # Ayushman card pending!
                "abha_number": "",
                "alive_status": "Alive",
                "remarks": "Daily wage worker. Encouraged to apply for Ayushman card.",
            }
        )

        # Yadav Parivar Members
        Member.objects.get_or_create(
            family=fam3,
            name="Devi Lal Yadav",
            defaults={
                "gender": "Male",
                "blood_group": "AB+",
                "relation": "Grandfather",
                "date_of_birth": datetime.date(1955, 1, 12),
                "religion": "Hindu",
                "caste": "OBC",
                "bpl": True,
                "bpl_number": "BPL-UP-2022-4412",
                "mobile_number": "9723456789",
                "aadhaar_number": "781290345612",
                "ayushman_card_number": "PMJAY-7812903456",
                "abha_number": "14-7812-9034-5612",
                "alive_status": "Alive",
                "disease": "Type 2 Diabetes, Joint Arthritis",
                "remarks": "Monthly blood sugar monitoring required.",
            }
        )

        Member.objects.get_or_create(
            family=fam3,
            name="Anita Yadav",
            defaults={
                "gender": "Female",
                "blood_group": "B+",
                "relation": "Mother",
                "date_of_birth": datetime.date(1988, 7, 22),
                "religion": "Hindu",
                "caste": "OBC",
                "bpl": True,
                "bpl_number": "BPL-UP-2022-4412",
                "mobile_number": "9723456789",
                "aadhaar_number": "781290345613",
                "ayushman_card_number": "",  # Ayushman pending
                "abha_number": "14-7812-9034-5613",
                "alive_status": "Alive",
                "remarks": "Needs Ayushman card enrollment.",
            }
        )

        # Ansari Family Members
        Member.objects.get_or_create(
            family=fam4,
            name="Fatima Ansari",
            defaults={
                "gender": "Female",
                "blood_group": "O+",
                "relation": "Mother",
                "date_of_birth": datetime.date(1993, 2, 8),
                "religion": "Muslim",
                "caste": "General",
                "bpl": False,
                "mobile_number": "9898765432",
                "aadhaar_number": "654321987654",
                "ayushman_card_number": "PMJAY-6543219876",
                "abha_number": "14-6543-2198-7654",
                "alive_status": "Alive",
                "remarks": "Healthy. Child immunization schedule on track.",
            }
        )

        Member.objects.get_or_create(
            family=fam4,
            name="Zainab Ansari",
            defaults={
                "gender": "Female",
                "blood_group": "O+",
                "relation": "Daughter",
                "date_of_birth": datetime.date(2023, 8, 14),
                "religion": "Muslim",
                "caste": "General",
                "bpl": False,
                "mobile_number": "9898765432",
                "aadhaar_number": "654321987655",
                "ayushman_card_number": "",
                "abha_number": "",
                "alive_status": "Alive",
                "remarks": "MR 1st dose administered. Growth chart in green zone.",
            }
        )
        self.stdout.write(self.style.SUCCESS("Members verified."))

        # 5. Seed Attendance Logs
        # Past 10-14 days records leading up to today
        duty_samples = [
            ("Routine Sub-Center Duty", "Present", v1, 4, 18, "Sub-center OPD, vitals recording, ORS distribution", datetime.time(9, 0), datetime.time(17, 0)),
            ("Home Visits & Door-to-Door Survey", "Field Duty", v1, 12, 26, "House 1 to 15 door-to-door visit, nutrition survey", datetime.time(9, 15), datetime.time(17, 30)),
            ("Maternal & Child Health Checkup", "Field Duty", v2, 8, 15, "ANC checkups for 3 pregnant mothers, HB testing", datetime.time(9, 0), datetime.time(16, 45)),
            ("Pulse Polio / Immunization Drive", "Camp Duty", v3, 6, 42, "Village booth immunization, 42 infants vaccinated", datetime.time(8, 30), datetime.time(16, 0)),
            ("Ayushman / ABHA Registration Camp", "Camp Duty", v1, 2, 35, "Assisted 12 families in Ayushman and ABHA card registration", datetime.time(9, 0), datetime.time(17, 15)),
            ("PHC / CHC Meeting & Training", "Present", None, 0, 5, "Monthly sector review meeting at Community Health Centre", datetime.time(10, 0), datetime.time(16, 30)),
            ("Home Visits & Door-to-Door Survey", "Field Duty", v2, 14, 29, "Postnatal care visits and new family enumeration", datetime.time(9, 0), datetime.time(17, 0)),
            ("Routine Sub-Center Duty", "Present", v1, 3, 16, "Weekly immunisation day at sub-centre", datetime.time(9, 5), datetime.time(17, 10)),
        ]

        for i, sample in enumerate(duty_samples):
            log_date = today - datetime.timedelta(days=(len(duty_samples) - i))
            # skip Sundays
            if log_date.weekday() == 6:
                log_date = log_date - datetime.timedelta(days=1)
            
            Attendance.objects.get_or_create(
                date=log_date,
                defaults={
                    "duty_type": sample[0],
                    "status": sample[1],
                    "village": sample[2],
                    "home_visits_count": sample[3],
                    "patients_attended": sample[4],
                    "tasks_completed": sample[5],
                    "check_in_time": sample[6],
                    "check_out_time": sample[7],
                    "remarks": "Duty completed as per schedule.",
                }
            )

        # Today's attendance: Active / Checked-in!
        Attendance.objects.get_or_create(
            date=today,
            defaults={
                "duty_type": "Home Visits & Door-to-Door Survey",
                "status": "Field Duty",
                "village": v1,
                "home_visits_count": 5,
                "patients_attended": 11,
                "tasks_completed": "Morning door-to-door visit in Shanti Nagar Ward 2. ANC follow-up for Pooja Sharma completed.",
                "check_in_time": datetime.time(8, 55),
                "check_out_time": None,  # Checked in today, duty ongoing!
                "remarks": "Check-out pending at end of day.",
            }
        )

        self.stdout.write(self.style.SUCCESS("Attendance records seeded."))
        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
