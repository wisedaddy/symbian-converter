import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ConverterApp extends JPanel {
    private JLabel googleFileLabel;
    private JTextField txtGoogleFile;
    private JButton googleFileButton;
    private JLabel outDirLabel;
    private JTextField txtOutDir;
    private JButton outDirButton;
    private JButton goButton;
    private static JFrame mainFrame;

    public ConverterApp() {
        super(new GridBagLayout());

        txtGoogleFile = new JTextField();
        txtGoogleFile.setColumns(30);
        txtOutDir = new JTextField();
        txtOutDir.setColumns(30);
        googleFileButton = new JButton("Select file");
        outDirButton = new JButton("Choose directory");
        goButton = new JButton("Go");

        GridBagConstraints c = new GridBagConstraints();
        c.gridx = 0;
        c.gridy = 0;
        add(new JLabel("Google VCF file"), c);
        c.gridy = 1;
        add(txtGoogleFile, c);
        c.gridx = 1;
        add(googleFileButton, c);

        c.gridx = 0;
        c.gridy = 2;
        add(new JLabel("Output directory"), c);
        c.gridy = 3;
        add(txtOutDir, c);
        c.gridx = 1;
        add(outDirButton, c);

        c.gridx = 1;
        c.gridy = 4;
        add(goButton, c);

        googleFileButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser chooser = new JFileChooser();
                chooser.setCurrentDirectory(new java.io.File("."));
                chooser.setDialogTitle("Select Google VCF contacts file");

                if (chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
                    txtGoogleFile.setText(chooser.getSelectedFile().getAbsolutePath());
                }
            }
        });
        goButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new Processor().process(txtGoogleFile.getText(), txtOutDir.getText());
                JOptionPane.showMessageDialog(mainFrame, "Done");
            }
        });
        outDirButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser chooser = new JFileChooser();
                chooser.setCurrentDirectory(new java.io.File("."));
                chooser.setDialogTitle("Choose output directory");
                chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
                chooser.setAcceptAllFileFilterUsed(false);

                if (chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
//                    System.out.println(chooser.getSelectedFile().getAbsolutePath());
                    txtOutDir.setText(chooser.getSelectedFile().getAbsolutePath());
                }
            }
        });

    }

    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */
    private static void createAndShowGUI() {
        //Create and set up the window.
        mainFrame = new JFrame("Google to Symbian VCard converter");
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Create and set up the content pane.
        ConverterApp form = new ConverterApp();
        form.setOpaque(true); //content panes must be opaque
        mainFrame.setContentPane(form);

        //Display the window.
        mainFrame.pack();
        mainFrame.setVisible(true);
    }

    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }

}
