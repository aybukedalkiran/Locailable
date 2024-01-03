from django.test import TestCase, TransactionTestCase
from django.db import transaction
from business.models import Business, Availability, Review
from users.models import Profile

class BusinessModelTests(TestCase):

    def test_create_business(self):
        business = Business.objects.create(
            business_name="Test Business",
            address="Test Address",
        )
        self.assertEqual(Business.objects.count(), 1)
        self.assertEqual(business.business_name, "Test Business")

    def test_create_availability(self):
        business = Business.objects.create(
            business_name="Test Business",
            address="Test Address",
        )
        availability = Availability.objects.create(
            business=business,
            total_tables=10,
            booked_tables=5,
        )
        self.assertEqual(Availability.objects.count(), 1)
        self.assertEqual(availability.business.business_name, "Test Business")
        self.assertEqual(availability.occupancy_ratio, 50.0)

    def test_create_review(self):
        profile = Profile.objects.create(
            username="test_user",
            email="test@example.com",
            bio="Test Bio",
        )
        business = Business.objects.create(
            business_name="Test Business",
            address="Test Address",
        )
        review = Review.objects.create(
            owner=profile,
            business=business,
            body="Test Review",
            value="up",
        )
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(review.owner.username, "test_user")
        self.assertEqual(review.business.business_name, "Test Business")
        self.assertEqual(review.value, "up")

    @transaction.atomic
    def test_transaction_Z(self):
        business = Business.objects.create(
            business_name="Test Business",
            address="Test Address",
        )
        availability = Availability.objects.create(
            business=business,
            total_tables=10,
            booked_tables=5,
        )
        self.assertEqual(Availability.objects.count(), 1)
        self.assertEqual(availability.business.business_name, "Test Business")
        self.assertEqual(availability.occupancy_ratio, 50.0)

    @transaction.atomic
    def test_transaction_W(self):
        with self.assertRaises(Exception):
            business = Business.objects.create(
                business_name="Test Business",
                address="Test Address",
            )

            raise Exception("Something went wrong!")

            availability = Availability.objects.create(
                business=business,
                total_tables=10,
                booked_tables=5,
            )
            self.assertEqual(Availability.objects.count(), 1)
            self.assertEqual(availability.business.business_name, "Test Business")
            self.assertEqual(availability.occupancy_ratio, 50.0)
