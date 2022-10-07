import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.io.File;
import java.io.IOException;
import java.nio.MappedByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;

public class User {
    int x, y, id;
    List<String> card = new ArrayList<>();
    User(int x, int y, int id){
        this.id = id;
        this.x = x;
        this.y = y;
    }
}
class json {
    public static boolean write(String src, String user) throws IOException {

        File file = new File(src);
        if (!file.exists()) {
            file.createNewFile();
            try (FileChannel channel = (FileChannel) Files.newByteChannel(Paths.get(src),
                    StandardOpenOption.WRITE, StandardOpenOption.CREATE,StandardOpenOption.READ)) {
                MappedByteBuffer MBB = channel.map(FileChannel.MapMode.READ_WRITE, 0, user.length());
                for (int i = 0; i < user.toCharArray().length; i++) {
                    MBB.put((byte) user.charAt(i));
                }
                return true;
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            try (FileChannel channel = (FileChannel) Files.newByteChannel(Paths.get(src),
                    StandardOpenOption.WRITE, StandardOpenOption.CREATE,StandardOpenOption.READ)) {
                MappedByteBuffer MBB = channel.map(FileChannel.MapMode.READ_WRITE, 0, user.length());
                for (int i = 0; i < user.toCharArray().length; i++) {
                    MBB.put((byte) user.charAt(i));
                }
                return true;
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return false;
    }
}
class test{
    public static void main(String[] args) throws IOException {
        User user = new User(0,0,0);
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        String src = "SomeThingShitOnJava/src/main/resources\\User.json";
        System.out.println(json.write(src,gson.toJson(user)));
    }
}
