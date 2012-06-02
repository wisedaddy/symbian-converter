import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.net.QuotedPrintableCodec;

import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.charset.CharacterCodingException;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;

public class VcfConverter {

    private static final String PAR_VAL_DELIM = ":";

    private QuotedPrintableCodec codec = new QuotedPrintableCodec();

    public String convert(String str) {
        int delim = str.indexOf(PAR_VAL_DELIM);
        if (delim < 0)
            return str;

        String par = str.substring(0, delim);
        String val = str.substring(delim + 1);
        if (!isPureAscii(val)) {
            par = par + ";ENCODING=QUOTED-PRINTABLE;CHARSET=UTF-8";
            val = convertToUtf8(val);
//            System.out.println(par);
//            System.out.println(val);
        }

        StringBuilder sb = new StringBuilder();
        return par + PAR_VAL_DELIM + val;
    }

    private boolean isPureAscii(String v) {
        byte bytearray[] = v.getBytes();
        CharsetDecoder d = Charset.forName("US-ASCII").newDecoder();
        try {
            CharBuffer r = d.decode(ByteBuffer.wrap(bytearray));
            r.toString();
        } catch (CharacterCodingException e) {
            return false;
        }
        return true;
    }

    private String convertToUtf8(String src) {
        try {
            return codec.encode(src);
        } catch (EncoderException e) {
            e.printStackTrace();  //To change body of catch statement use File | Settings | File Templates.
        }
        return src;
    }

}
