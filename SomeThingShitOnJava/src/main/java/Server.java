import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static final int PORT = 5690;
    public static void main(String ... str) throws IOException {
        ServerSocket server = new ServerSocket(PORT);

    }
}
class UserSocket extends Thread{
    private Socket socket;
    private BufferedReader in;
    private BufferedWriter out;
    public UserSocket(Socket socket) throws IOException {
        this.socket = socket;
        in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        out = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));
        start();
    }

    @Override
    public void run() {
        String word;
        try{
            while (true){
                word = in.readLine();
                if (word.equals("stop")) break;

            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
