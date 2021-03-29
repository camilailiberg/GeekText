from django.urls import path
from register import views

urlpatterns = [
    path("", views.register, name="register"),
    path("account", views.account, name="account"),
    path("edit_username", views.edit_username, name= "edit_username"),
    path("edit_email", views.edit_email, name="edit_email"),
    path("edit_first_name", views.edit_first_name, name="edit_first_name"),
    path("edit_last_name", views.edit_last_name, name="edit_last_name"),
    path("edit_home_address", views.edit_home_address, name="edit_home_address"),
    path("edit_address", views.edit_address, name="edit_address"),
    path("edit", views.edit, name="edit"),
    path("payment_information/<int:errormessage>", views.payment_info, name="payment_info"),
    path("add_credit_card_information", views.add_credit_card_info, name="add_credit_card_info"),
    path("edit_credit_card_information/<int:creditcardid>/<int:error>", views.edit_credit_card_info, name="edit_credit_card_info"),
    path("delete_credit_card_information/<int:creditcardid>", views.delete_credit_card_info,
         name="delete_credit_card_info"),
    path("change_password", views.change_password, name="change_password"),
]
