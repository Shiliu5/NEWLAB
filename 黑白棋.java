import java.util.Scanner;

public class OthelloGame {
    private char[][] board;
    private char currentPlayer;

    public OthelloGame() {
        board = new char[8][8];
        currentPlayer = 'B'; // 黑棋先手
        initializeBoard();
    }

    private void initializeBoard() {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                board[i][j] = '-';
            }
        }
        board[3][3] = 'W';
        board[3][4] = 'B';
        board[4][3] = 'B';
        board[4][4] = 'W';
    }

    private void printBoard() {
        System.out.println("  0 1 2 3 4 5 6 7");
        for (int i = 0; i < 8; i++) {
            System.out.print(i + " ");
            for (int j = 0; j < 8; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    private boolean isValidMove(int row, int col) {
        if (row < 0 || row >= 8 || col < 0 || col >= 8 || board[row][col] != '-') {
            return false;
        }
        int[] directions = {-1, 0, 1};
        for (int dx : directions) {
            for (int dy : directions) {
                if (dx == 0 && dy == 0) {
                    continue;
                }
                int r = row + dx;
                int c = col + dy;
                boolean foundOpponent = false;
                while (r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] != '-') {
                    if (board[r][c] == currentPlayer) {
                        if (foundOpponent) {
                            return true;
                        } else {
                            break;
                        }
                    } else {
                        foundOpponent = true;
                    }
                    r += dx;
                    c += dy;
                }
            }
        }
        return false;
    }

    private void makeMove(int row, int col) {
        board[row][col] = currentPlayer;
        int[] directions = {-1, 0, 1};
        for (int dx : directions) {
            for (int dy : directions) {
                if (dx == 0 && dy == 0) {
                    continue;
                }
                int r = row + dx;
                int c = col + dy;
                boolean foundOpponent = false;
                while (r >= 0 && r < 8 && c >= 0 && c < 8 && board[r][c] != '-') {
                    if (board[r][c] == currentPlayer) {
                        if (foundOpponent) {
                            int dr = dx;
                            int dc = dy;
                            while (r != row || c != col) {
                                r -= dr;
                                c -= dc;
                                board[r][c] = currentPlayer;
                            }
                            break;
                        } else {
                            break;
                        }
                    } else {
                        foundOpponent = true;
                    }
                    r += dx;
                    c += dy;
                }
            }
        }
    }

    private boolean hasValidMove() {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (isValidMove(i, j)) {
                    return true;
                }
            }
        }
        return false;
    }

    private void switchPlayer() {
        currentPlayer = (currentPlayer == 'B') ? 'W' : 'B';
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            printBoard();
            System.out.println("当前玩家: " + currentPlayer);
            if (!hasValidMove()) {
                switchPlayer();
                if (!hasValidMove()) {
                    break;
                }
                continue;
            }
            System.out.print("请输入要落子的行号和列号，以空格分隔：");
            int row = scanner.nextInt();
            int col = scanner.nextInt();
            if (isValidMove(row, col)) {
                makeMove(row, col);
                switchPlayer();
            } else {
                System.out.println("无效的落子，请重新输入。");
            }
        }
        printBoard();
        int blackCount = 0;
        int whiteCount = 0;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (board[i][j] == 'B') {
                    blackCount++;
                } else if (board[i][j] == 'W') {
                    whiteCount++;
                }
            }
        }
        System.out.println("游戏结束。");
        System.out.println("黑棋数量: " + blackCount);
        System.out.println("白棋数量: " + whiteCount);
        if (blackCount > whiteCount) {
            System.out.println("黑棋获胜！");
        } else if (blackCount < whiteCount) {
            System.out.println("白棋获胜！");
        } else {
            System.out.println("平局！");
        }
    }

    public static void main(String[] args) {
        OthelloGame game = new OthelloGame();
        game.play();
    }
}
