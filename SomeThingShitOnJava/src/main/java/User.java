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
    private static File file;
    private static String user, src;
    json(String src, String user) throws IOException {
        file = new File(src);
        this.user = user;
        this.src = src;
        if (!file.exists()){
            file.createNewFile();
            write();
        }else write();
    }


    private static boolean write() throws IOException {
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
        return false;
    }



}
