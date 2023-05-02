import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class DrawingDemo extends JPanel {
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.RED);
        g.fillRect(10, 10, 100, 100);
        g.setColor(Color.BLUE);
        g.fillOval(150, 10, 100, 100);
        g.setColor(Color.GREEN);
        g.drawLine(300, 10, 400, 110);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Drawing Demo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 200);
        frame.getContentPane().add(new DrawingDemo());
        frame.setVisible(true);
    }
}
