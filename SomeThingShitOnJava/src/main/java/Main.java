import py4j.GatewayServer;

public class Main {
    public static void main(String ... str){
        GatewayServer server = new GatewayServer();
        server.start();
    }
}
