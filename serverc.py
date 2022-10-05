import socket
import pickle 
import allocate_sym

from tic_tac_toec import TicTacToe

HOST = '127.0.0.1' 
PORT = 12783        

# server set up
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
allocate_sym.init()

# accept a connection
client_socket, client_address = s.accept()
print(f"\nConnnected to {client_address}!\n")

# set up the game
while True:
    host_sym =input("Enter X or O: ")
    if host_sym.capitalize() == "X" or host_sym.capitalize()==host_sym:
        break
    else:
        print("Enter Valid Input either 'X' or 'O'")
# host_sym = "X"
if host_sym == 'X':
    cli_sym = "O"
else:
    cli_sym = "X"
client_socket.send(host_sym.encode())
# cli_sym = "O"
print(host_sym)
player_x = TicTacToe(host_sym)

rematch = True

while rematch == True: 
    print(f"\n TIC-TAC-TOE ")

    # it exits the loop if when either one player wins 
    # while player_x.did_win(host_sym) == False and player_x.did_win(host_sym) == False and player_x.is_draw() == False:
    while player_x.is_draw() == False and player_x.did_win(host_sym) == False and player_x.did_win(cli_sym) == False:
        print(f"\n  Now Your turn!")
        player_x.draw_grid()
        # if input() == NULL:
        #     coords = input("Enter the coordinate: ")
        # else:
        #     coords = input("Enter the coordinate: ")
        coords = input("Enter the coordinate: ")
        player_x.edit_square(coords)

        # draw grid again
        player_x.draw_grid()

        # send the symbol list using pickle
        x_symbol_list = pickle.dumps(player_x.symbols_list)
        print(player_x.symbols_list)
        client_socket.send(x_symbol_list)

        # check whether player win or not
        if player_x.did_win(host_sym) == True or player_x.is_draw() == True:
            break

        # load the symbol list using pickle
        print(f"\nWaiting for other player...")
        o_symbol_list = client_socket.recv(1024)
        o_symbol_list = pickle.loads(o_symbol_list)
        player_x.update_symbol_list(o_symbol_list)

    # check who is an winner or it is a draw
    if player_x.did_win(host_sym) == True:
        print(f"Congrats, you won!")
        allocate_sym.host_win += 1
    elif player_x.is_draw() == True:
        print(f"It's a draw!")
    else:
        print(f"Sorry, the client won.")
        allocate_sym.cli_win += 1

    #rematch
    host_response = input(f"\nRematch? (Y/N): ")
    host_response = host_response.capitalize()
    temp_host_resp = host_response
    client_response = ""

    # send the host response using pickle 
    host_response = pickle.dumps(host_response)
    client_socket.send(host_response)

    if temp_host_resp == "N":
        rematch = False

    #client opinion
    else:
        # receiving client's response 
        print(f"Waiting for client response...")
        client_response = client_socket.recv(1024)
        client_response = pickle.loads(client_response)

        if client_response == "N":
            print(f"\nThe client does not want a rematch.")
            rematch = False

        else:
            player_x.restart_game()

# spacer = input(f"\nThank you for playing!\nPress enter to quit...\n")
spacer = input(f"\nThank you for playing!\nYour score:{allocate_sym.host_win}\t opponent score:{allocate_sym.cli_win}\nPress enter to quit...\n")


client_socket.close()