import java.io.*;

public class Processor {

    private VcfConverter converter = new VcfConverter();

    public void process(String src, String dst) {
        try {
            BufferedReader br = new BufferedReader(new FileReader(src));
            String strLine;
            BufferedWriter bw = null;
            //Read File Line By Line
            while ((strLine = br.readLine()) != null) {
                // Print the content on the console
                if ("BEGIN:VCARD".equals(strLine)) {
                    if (bw != null) {
                        bw.close();
                    }
                    bw = new BufferedWriter(new FileWriter(File.createTempFile("contact_", ".vcf", new File(dst))));
                }

                if (bw != null) {
                    bw.write(converter.convert(strLine));
                    bw.write("\r\n");
                }
            }
            br.close();
            if (bw != null) {
                bw.close();
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();  //To change body of catch statement use File | Settings | File Templates.
        } catch (IOException e) {
            e.printStackTrace();  //To change body of catch statement use File | Settings | File Templates.
        }
    }

    public static void main(String[] args) {

    }

}
