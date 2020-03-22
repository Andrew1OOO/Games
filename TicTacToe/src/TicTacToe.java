import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class TicTacToe extends JFrame implements MouseListener{

        int mousex;
        int mousey;
        int game_over = 0;
        String current_player = "X";

        String squares[] = new String[9];


        public TicTacToe() {
           squares[0] = " ";
           squares[1] = " ";
           squares[2] = " ";
           squares[3] = " ";
           squares[4] = " ";
           squares[5] = " ";
           squares[6] = " ";
           squares[7] = " ";
           squares[8] = " ";


            setSize (400, 400);
            setVisible (true);
            setDefaultCloseOperation(EXIT_ON_CLOSE);
            addMouseListener(this);



        }

        public void mouseClicked(MouseEvent e) {

            int chosen_square = 0;

            if (game_over == 0) {

            mousex = e.getX();
            mousey = e.getY();
            if (mousey >= 250) {
                chosen_square +=6;
            }
            else if (mousey >= 150) {
                chosen_square +=3;
            }

            if (mousex >= 250) {
                chosen_square +=2;
            }
            else if (mousex >= 150) {
                chosen_square +=1;
            }
            squares[chosen_square] = current_player;

        }
         if (((squares[0] == current_player) && (squares[1] == current_player) && (squares[2] == current_player)) ||
            ((squares[3] == current_player) && (squares[4] == current_player) && (squares[5] == current_player)) ||
            ((squares[6] == current_player) && (squares[7] == current_player) && (squares[8] == current_player)) ||
            ((squares[0] == current_player) && (squares[3] == current_player) && (squares[6] == current_player)) ||
            ((squares[1] == current_player) && (squares[4] == current_player) && (squares[7] == current_player)) ||
            ((squares[2] == current_player) && (squares[5] == current_player) && (squares[8] == current_player)) ||
            ((squares[0] == current_player) && (squares[4] == current_player) && (squares[8] == current_player)) ||
            ((squares[2] == current_player) && (squares[4] == current_player) && (squares[6] == current_player))){
            game_over = 1;
            setBackground(Color.YELLOW);
            setForeground(Color.RED);

            }

         else if ((squares[0]=="X"|| squares[0]=="O") &&
                 (squares[1]=="X"|| squares[1]=="O") &&
                 (squares[2]=="X"|| squares[2]=="O") &&
                 (squares[3]=="X" || squares[3]=="O") &&
                 (squares[4] == "X" || squares[4] == "O") &&
                 (squares[5]=="X" || squares[5]=="O") &&
                 (squares[6]=="X" || squares[6]=="O") &&
                 (squares[7] == "X" || squares[7] == "O") &&
                 (squares[8]=="X" || squares[8]=="O")){
             game_over = 1;
             setBackground(Color.BLUE);
             setForeground(Color.YELLOW);

            }
            else {
            if (current_player == "X") {
                current_player = "O";
            }
            else {
                current_player = "X";
            }
        }

            repaint();
        }


        public void mouseExited(MouseEvent e) {
            mousex = e.getX();
            mousey = e.getY();
        }

        public void mouseEntered(MouseEvent e) {
            mousex = e.getX();
            mousey = e.getY();
        }

        public void mousePressed(MouseEvent e) {
            mousex = e.getX();
            mousey = e.getY();
        }

        public void mouseReleased(MouseEvent e) {
            mousex = e.getX();
            mousey = e.getY();
        }

        public void paint (Graphics g) {
           g.drawLine(150,50,150,350);
           g.drawLine(250,50,250,350);
           g.drawLine(50,150,350,150);
           g.drawLine(50,250,350,250);

           int base_square_x = -50;
           int base_square_y = 50;



           for (int i = 0; i < 9; i++) {

               base_square_x += 100;

               if ((i == 3) || (i == 6)) {
                   base_square_x = 50;
                   base_square_y += 100;
                }


               if (squares[i] == "O") {
                   g.drawOval(base_square_x+18,base_square_y+18,64,64);
                }

               if (squares [i] == "X") {
                   g.drawLine(base_square_x+18, base_square_y+18, base_square_x+82,base_square_y+82);
                   g.drawLine(base_square_x+82,base_square_y+18, base_square_x+18,base_square_y+82);
                }
            }
        }


    }
