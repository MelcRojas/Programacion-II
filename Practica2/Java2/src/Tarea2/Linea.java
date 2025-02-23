package Tarea2;

import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;
class Punto {
    int x, y;

    public Punto(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Linea extends JPanel {
    public Punto p1;
    public Punto p2;
    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
    }

    @Override
    public String toString() {
        return "Linea [p1=(" + p1.x + "," + p1.y + "), p2=(" + p2.x + "," + p2.y + ")]";
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        g.drawLine(p1.x, p1.y, p2.x, p2.y);
    }

    public static void main(String[] args) {
        Punto punto1 = new Punto(200, 000);
        Punto punto2 = new Punto(200, 200);
        Linea objeto = new Linea(punto1, punto2);

        JFrame ventana = new JFrame("Grafico Linea");
        ventana.add(objeto);
        ventana.setSize(700, 700);
        ventana.setLocationRelativeTo(null);
        ventana.setVisible(true);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        System.out.println(objeto.toString()); 
    }
}
