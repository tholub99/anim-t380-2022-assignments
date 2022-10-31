using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PipelineMidterm
{
    public class Report
    {
        //Data
        string imagePath;
        string imageName;
        string imageArtist;
        string notesPath;
        List<Note> notes;

        //Form
        PictureBox pictureBox;
        FlowLayoutPanel noteLayoutPanel;
        Label imageLabel;
        
        public Report(Form1 parentForm, string imgPath, string ntsPath)
        {
            imagePath = imgPath;
            notesPath = ntsPath;
            imageName = Path.GetFileNameWithoutExtension(imgPath);

            InitializeReportForm(parentForm);
            HideReport();
            ImportExistingNotes();

            pictureBox.ImageLocation = imagePath;
            imageLabel.Text = String.Format("{0} by {1}", imageName, imageArtist);
        }

        private void ImportExistingNotes()
        {
            bool firstLineRead = false;
            notes = new List<Note>();
            foreach (string line in File.ReadLines(notesPath))
            {
                if(!firstLineRead)
                {
                    imageArtist = line;
                    firstLineRead = true;
                    continue;
                }    

                Note note = new Note(this, noteLayoutPanel);
                note.SetText(line);
                notes.Add(note);
            }
        }

        private void InitializeReportForm(Form1 form)
        {
            pictureBox = new PictureBox();
            pictureBox.Location = new Point(12, 69);
            pictureBox.Size = new Size(480, 264);
            pictureBox.SizeMode = PictureBoxSizeMode.Zoom;
            form.Controls.Add(pictureBox);

            noteLayoutPanel = new FlowLayoutPanel();
            noteLayoutPanel.FlowDirection = FlowDirection.TopDown;
            noteLayoutPanel.AutoScroll = true;
            noteLayoutPanel.WrapContents = false;
            noteLayoutPanel.Location = new Point(12, 374);
            noteLayoutPanel.Size = new Size(480, 260);
            form.Controls.Add(noteLayoutPanel);

            imageLabel = new Label();
            imageLabel.Location = new Point(66, 46);
            imageLabel.Size = new Size(280, 20);
            form.Controls.Add(imageLabel);
        }

        private string[] CombineNotesToArray()
        {
            List<string> noteList = new List<string>();
            foreach(Note note in notes)
            {
                noteList.Add(note.GetText());
            }
            return noteList.ToArray();
        }

        public void HideReport()
        {
            imageLabel.Hide();
            pictureBox.Hide();
            noteLayoutPanel.Hide();
        }

        public void ShowReport()
        {
            imageLabel.Show();
            pictureBox.Show();
            noteLayoutPanel.Show();
        }

        public void AddNote()
        {
            notes.Add(new Note(this, noteLayoutPanel));
        }

        public void RemoveNote(Note note)
        {
            notes.Remove(note);
        }

        public string GenerateReportBody()
        {
            string LINE_BREAK = "%0D%0A";
            string body = String.Format("Image Location: {0}{1}", imagePath, LINE_BREAK);
            for (int i = 0; i < notes.Count; i++)
            {
                Note note = notes[i];
                body += String.Format("Note {0}: {1}", i + 1, note.GetText());
                if (i != notes.Count - 1)
                {
                    body += LINE_BREAK;
                }
            }

            return body;
        }

        public string GenerateReportCSV()
        {
            string CSV = String.Format("{0},{1},{2}", imagePath, imageArtist, String.Join(",", CombineNotesToArray()));
            return CSV;
        }

        public string GetImagePath()
        {
            return imagePath;
        }
    }
}
