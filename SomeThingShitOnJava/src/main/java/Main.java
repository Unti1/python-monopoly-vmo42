import py4j.GatewayServer;

import java.util.ArrayList;

public class Main {
    public static void main(String ... str){
        GatewayServer server = new GatewayServer(new ArrayList<String>());
        server.start();
    }
}
