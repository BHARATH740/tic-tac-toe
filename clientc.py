import socket 
import pickle  
import allocate_sym

from tic_tac_toec import TicTacToe

HOST = '127.0.0.1'   
PORT = 12783        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"\nConnected to {s.getsockname()}!")
allocate_sym.init()

# client set up
host_sym = s.recv(1024).decode()
print(host_sym)
# host_sym = "X"
if host_sym == 'X':
    cli_sym = "O"
else:
    cli_sym = "X"
print(f"Your symbol is : {cli_sym}")
player_o = TicTacToe(cli_sym)


rematch = True

while rematch == True:
    print(f"\n\n TIC-TAC-TOE ")

    player_o.draw_grid()

    # waiting for host to play:
    print(f"\nWaiting for other player...")
    x_symbol_list = s.recv(1024)
    x_symbol_list = pickle.loads(x_symbol_list)
    player_o.update_symbol_list(x_symbol_list)

    # it exits the loop if when either one player wins 
    while player_o.did_win(cli_sym) == False and player_o.did_win(host_sym) == False and player_o.is_draw() == False:
        print(f"\n       Your turn!")
        player_o.draw_grid()
        player_coord = input(f"Enter coordinate: ")
        player_o.edit_square(player_coord)

        # draw grid again
        player_o.draw_grid()

        # send the symbol list using pickle
        o_symbol_list = pickle.dumps(player_o.symbols_list)
        s.send(o_symbol_list)

        # check whether player win or not
        if player_o.did_win(cli_sym) == True or player_o.is_draw() == True:
            break

        # load the symbol list using pickle
        print(f"\nWaiting for other player...")
        x_symbol_list = s.recv(1024)
        x_symbol_list = pickle.loads(x_symbol_list)
        player_o.update_symbol_list(x_symbol_list)

    # check who is an winner or it is a draw
    if player_o.did_win(cli_sym) == True:
        print(f"Congrats, you won!")
        allocate_sym.cli_win +=1
    elif player_o.is_draw() == True:
        print(f"It's a draw!")
    else:
        print(f"Sorry, the host won.")
        allocate_sym.host_win +=1

    #rematch
    print(f"\nWaiting for host...")
    host_response = s.recv(1024)
    host_response = pickle.loads(host_response)
    client_response = "N"

    # askinng client
    if host_response == "Y":
        print(f"\nThe host would like a rematch!")
        client_response = input("Rematch? (Y/N): ")
        client_response = client_response.capitalize()
        temp_client_resp = client_response

        # recieving client response
        client_response = pickle.dumps(client_response)
        s.send(client_response)

        if temp_client_resp == "Y":
            player_o.restart_game()

        else:
            rematch = False

    else:
        print(f"\nThe host does not want a rematch.")
        rematch = False

spacer = input(f"\nThank you for playing!\nYour score:{allocate_sym.cli_win}\t opponent score:{allocate_sym.host_win}\nPress enter to quit...\n")

s.close()