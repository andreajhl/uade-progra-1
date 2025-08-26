from tools.init_hall import init_hall
from interface.ask_ticket_count import ask_ticket_count
from interface.input_free_seat import input_free_seat
from tools.set_busy_seat import set_busy_seat
from interface.show_hall import show_hall


def main():
    
    hall = init_hall()

    while True:
        count = ask_ticket_count(hall)

        if count == 0:
            print("Sala llena")
            return

        purchased = 0

        while purchased < count:
            row, column = input_free_seat(hall)
            set_busy_seat(row, column, hall)

            print(f"Seleccionaste la butaca F{row+1}-C{column+1}.")
        
            purchased += 1

        print(f"Compra finalizada. Entradas adquiridas: {purchased}.")
        show_hall(hall)


if __name__ == "__main__":
    main()