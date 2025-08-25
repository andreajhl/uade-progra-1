from products.tickets import buy_tickets
from admin.hall import create_halls

hall = create_halls()
buy_tickets(hall)