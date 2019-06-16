import java.io.*;
import java.net.*;

public class Rest {

    public static void main(String[] args) throws IOException {
        URL url = new URL("http://localhost:8000/api/works/test_multiple/");
        String query = "{id:13456}";

        //make connection
        URLConnection urlc = url.openConnection();

        //use post mode
        urlc.setDoOutput(true);
        urlc.setAllowUserInteraction(false);

        //send query
        PrintStream ps = new PrintStream(urlc.getOutputStream());
        // ps.print(query);
        ps.close();

        //get result
        BufferedReader br = new BufferedReader(new InputStreamReader(urlc
            .getInputStream()));
        String l = null;
        while ((l=br.readLine())!=null) {
            System.out.println(l);
        }
        br.close();
    }
}