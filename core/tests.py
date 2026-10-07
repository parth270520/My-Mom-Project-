from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from core.models import Village, Family, Member, Attendance


class AshaCareAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='asha',
            password='123456'
        )
        self.village = Village.objects.create(
            village_number=101,
            name='Test Shanti Nagar',
            total_houses=50
        )
        self.family = Family.objects.create(
            family_name='Sharma Family',
            village=self.village,
            house_number=1,
            contact_number='9876543210'
        )

    def test_login_flow(self):
        # GET login
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        # POST valid PIN
        response = self.client.post(reverse('login'), {'pin': '123456'})
        self.assertRedirects(response, reverse('dashboard'))

    def test_dashboard_authenticated(self):
        self.client.login(username='asha', password='123456')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('today_attendance', response.context)
        self.assertIn('total_families', response.context)
        self.assertIn('this_month_present_days', response.context)

    def test_attendance_list_and_quick_checkin(self):
        self.client.login(username='asha', password='123456')
        response = self.client.get(reverse('attendance_list'))
        self.assertEqual(response.status_code, 200)

        # Quick check-in
        response = self.client.post(reverse('mark_attendance'), {
            'action': 'quick_check_in',
            'next': 'attendance_list',
        })
        self.assertRedirects(response, reverse('attendance_list'))
        today = timezone.localdate()
        att = Attendance.objects.filter(date=today).first()
        self.assertIsNotNone(att)
        self.assertEqual(att.status, 'Present')
        self.assertIsNotNone(att.check_in_time)

        # Quick check-out
        response = self.client.post(reverse('mark_attendance'), {
            'action': 'quick_check_out',
            'next': 'dashboard',
        })
        self.assertRedirects(response, reverse('dashboard'))
        att.refresh_from_db()
        self.assertIsNotNone(att.check_out_time)

    def test_attendance_report(self):
        self.client.login(username='asha', password='123456')
        response = self.client.get(reverse('attendance_report'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Monthly Nurse Duty & Attendance Register")
