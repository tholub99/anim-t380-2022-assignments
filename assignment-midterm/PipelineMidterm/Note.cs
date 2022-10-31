using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PipelineMidterm
{
    public class Note
    {
        Report myReport;

        //Form
        Panel panel;
        TextBox textBox;
        Button button;

        public Note(Report parentReport, FlowLayoutPanel parentPanel)
        {
            myReport = parentReport;

            panel = new Panel();
            textBox = new TextBox();
            button = new Button();

            //Create new panel for note
            panel.Size = new Size(460, 48);
            panel.Parent = parentPanel;

            //Create new text box for note
            textBox.Multiline = true;
            textBox.Size = new Size(420, 48);
            textBox.Parent = this.panel;

            //Create new delete button for note
            button.Size = new Size(26, 26);
            button.Location = new Point(430, 14);
            button.Font = new Font(button.Font, FontStyle.Bold);
            button.Text = "X";
            button.ForeColor = Color.Red;

            button.Parent = this.panel;
            button.Click += new System.EventHandler(this.button_Click);
        }

        private void button_Click(object sender, EventArgs e)
        {
            panel.Dispose();
            myReport.RemoveNote(this);
        }

        public string GetText()
        {
            return this.textBox.Text;
        }

        public void SetText(string newText)
        {
            this.textBox.Text = newText;
        }
    }
}
