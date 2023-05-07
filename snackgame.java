import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.Random;

public class SnakeGame extends JFrame implements ActionListener {

    public static final int WIDTH = 800;
    public static final int HEIGHT = 800;
    public static final int GRID_SIZE = 25;
    public static final int GRID_WIDTH = WIDTH / GRID_SIZE;
    public static final int GRID_HEIGHT = HEIGHT / GRID_SIZE;

    private Timer timer;
    private int[] snakeX = new int[GRID_WIDTH * GRID_HEIGHT];
    private int[] snakeY = new int[GRID_WIDTH * GRID_HEIGHT];
    private int snakeLength;

    private int appleX;
    private int appleY;

    private boolean left, right, up, down;
    private boolean inGame;

    public SnakeGame() {
        setTitle("Snake Game");
        setSize(WIDTH, HEIGHT);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);

        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                int key = e.getKeyCode();

                if ((key == KeyEvent.VK_LEFT) && (!right)) {
                    left = true;
                    up = false;
                    down = false;
                }

                if ((key == KeyEvent.VK_RIGHT) && (!left)) {
                    right = true;
                    up = false;
                    down = false;
                }

                if ((key == KeyEvent.VK_UP) && (!down)) {
                    left = false;
                    up = true;
                    right = false;
                }

                if ((key == KeyEvent.VK_DOWN) && (!up)) {
                    left = false;
                    right = false;
                    down = true;
                }
            }
        });

        initGame();
    }

    public void initGame() {
        snakeLength = 3;
        for (int i = 0; i < snakeLength; i++) {
            snakeX[i] = GRID_WIDTH / 2 - i;
            snakeY[i] = GRID_HEIGHT / 2;
        }

        locateApple();

        timer = new Timer(140, this);
        timer.start();

        left = false;
        right = true;
        up = false;
        down = false;
        inGame = true;
    }

    private void locateApple() {
        Random random = new Random();
        appleX = random.nextInt(GRID_WIDTH);
        appleY = random.nextInt(GRID_HEIGHT);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        if (inGame) {
            g.setColor(Color.RED);
            g.fillRect(appleX * GRID_SIZE, appleY * GRID_SIZE, GRID_SIZE, GRID_SIZE);

            for (int i = 0; i < snakeLength; i++) {
                if (i == 0) {
                    g.setColor(Color.BLACK);
                } else {
                    g.setColor(Color.GREEN);
                }
                g.fillRect(snakeX[i] * GRID_SIZE, snakeY[i] * GRID_SIZE, GRID_SIZE, GRID_SIZE);
            }

            Toolkit.getDefaultToolkit().sync();
        } else {
            gameOver(g);
        }
    }

    private void gameOver(Graphics g) {
        String msg = "Game Over";
        Font small = new Font("Helvetica", Font.BOLD, 14);
        FontMetrics metr = getFontMetrics(small);

        g.setColor(Color.BLACK);
        g.setFont(small);
        g.drawString(msg, (WIDTH - metr.stringWidth(msg)) / 2, HEIGHT / 2);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (inGame) {
            checkApple();
            checkCollision();
            moveSnake();
        }

        repaint();
    }

    private void checkApple() {
        if ((snakeX[0] == appleX) && (snakeY[0] == appleY)) {
            snakeLength++;
            locateApple();
        }
    }

    private void checkCollision() {
        for (int i = snakeLength; i > 0; i--) {
            if ((i > 3) && (snakeX[0] == snakeX[i]) && (snakeY[0] == snakeY[i])) {
                inGame = false;
            }
        }

        if (snakeY[0] >= GRID_HEIGHT || snakeY[0] < 0 || snakeX[0] >= GRID_WIDTH || snakeX[0] < 0) {
            inGame = false;
        }

        if (!inGame) {
            timer.stop();
        }
    }

    private void moveSnake() {
        for (int i = snakeLength; i > 0; i--) {
            snakeX[i] = snakeX[(i - 1)];
            snakeY[i] = snakeY[(i - 1)];
        }

        if (left) {
            snakeX[0]--;
        }

        if (right) {
            snakeX[0]++;
        }

        if (up) {
            snakeY[0]--;
        }

        if (down) {
            snakeY[0]++;
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                JFrame frame = new SnakeGame();
                frame.setVisible(true);
            }
        });
    }
}
