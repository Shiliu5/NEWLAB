import javax.swing.*;
import java.awt.*;

public class SimpleDrawingProgram extends JFrame {

    public SimpleDrawingProgram() {
        setTitle("简单绘图程序");
        setSize(500, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        DrawingPanel drawingPanel = new DrawingPanel();
        add(drawingPanel);

        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new SimpleDrawingProgram());
    }

    private static class DrawingPanel extends JPanel {

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);

            // 绘制一个矩形
            g.drawRect(50, 50, 200, 100);

            // 绘制一个圆形
            g.drawOval(300, 200, 100, 100);

            // 绘制一条线段
            g.drawLine(100, 300, 400, 300);
        }
    }
}
