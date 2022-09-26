import py4j.GatewayServer;

import java.util.ArrayList;

class Player{
    private ArrayList<String> buildings;
    private int money;
    private String name;

    public Player(){
        buildings = new ArrayList<>();
    }

    public boolean addBuilding(String build){
        return buildings.add(build);
    }

    public boolean deleteBuilding(String build){
        return buildings.remove(build);
    }

    public ArrayList<String> getBuildings() {
        return buildings;
    }

    public void setMoney(int money) {
        this.money = money;
    }

    public int getMoney() {
        return money;
    }

    public String getName() {
        return name;
    }
}


public class Main {
    public static void main(String ... str){
        GatewayServer server = new GatewayServer(new Player());
        server.start();
        System.out.println("Сервер запущен");
    }
}
