from django.contrib import admin

from .models import Producer, DiscountProducer, LoyaltyProgram, ProducerCar


@admin.register(ProducerCar)
class ProducerCarAdmin(admin.ModelAdmin):
    list_display = (
        "car",
        "producer",
        "price",
        "count",
    )


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    readonly_fields = (
        "found_year",
        "description",
        "number_of_buyers",
    )
    list_filter = (
        "name",
        "country",
        "number_of_buyers",
        "is_active",
        "added_date",
        "date_updated",
    )


@admin.register(DiscountProducer)
class DiscountProducerAdmin(admin.ModelAdmin):
    list_filter = (
        "discount",
        "bought_cars",
        "producer",
    )


@admin.register(LoyaltyProgram)
class ProducerLoyaltyProgramAdmin(admin.ModelAdmin):
    readonly_fields = ("added_date", "date_updated")
    list_filter = ("producer", "program", "min_bought_cars", "is_active")
