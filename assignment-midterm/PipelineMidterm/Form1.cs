using System.Diagnostics;
using System.Security;

namespace PipelineMidterm
{
    public partial class Form1 : Form
    {
        public static string configDir;
        string imageDir;
        string notesDir;
        string exportDir;
        public static EmailList activeEmailList;
        public static Dictionary<string, EmailList> availableEmailLists;
        public static List<Report> reportList;

        int MIN_REPORT_INDEX = 0;
        int MAX_REPORT_INDEX;
        int currentReportIndex = 0;

        public static Report activeReport;
        Form2 emailForm;
        public Form1()
        {
            availableEmailLists = new Dictionary<string, EmailList>();
            reportList = new List<Report>();

            configDir = String.Format("{0}\\email_configs", Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.FullName);
            imageDir = String.Format("{0}\\images", Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.FullName);
            notesDir = String.Format("{0}\\image_notes", Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.FullName);
            exportDir = String.Format("{0}\\exports", Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.FullName);

            LoadAvailableReports();
            LoadAvailableEmailLists();

            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SetDefaultEmailList();
            activeReport = reportList[0];
            activeReport.ShowReport();
            textBox1.Text = activeReport.GetImagePath();
            button5.Enabled = false;
        }

        private void SetDefaultEmailList()
        {           
            activeEmailList = new EmailList(availableEmailLists["default"]);
        }

        private void LoadAvailableEmailLists()
        {
            DirectoryInfo dir = new DirectoryInfo(configDir);
            foreach (FileInfo file in dir.GetFiles())
            {
                EmailList newList = new EmailList(file.FullName);
                string title = newList.GetTitle();
                availableEmailLists.Add(title, newList);
            }
        }

        private void LoadAvailableReports()
        {
            DirectoryInfo dir = new DirectoryInfo(imageDir);
            foreach (FileInfo file in dir.GetFiles())
            {
                string notesPath = String.Format("{0}\\{1}.txt", notesDir, Path.GetFileNameWithoutExtension(file.FullName));
                Report report = new Report(this, file.FullName, notesPath);
                reportList.Add(report);
            }
            MAX_REPORT_INDEX = reportList.Count - 1;
        }

        private string GenerateEmailBody()
        {
            string LINE_BREAK = "%0D%0A";
            string body = "";
            foreach(Report report in reportList)
            {
                string reportBody = report.GenerateReportBody();
                body = String.Format("{0}{1}{2}{3}", body, LINE_BREAK, LINE_BREAK, reportBody);
            }
            return body;
        }

        private void ExportCSV()
        {
            List<string> csv = new List<string>()
            {
                "Path,Artist,Notes"
            };
            foreach(Report report in reportList)
            {
                string reportCSV = report.GenerateReportCSV();
                csv.Add(reportCSV);
            }
            File.WriteAllLines(String.Format("{0}\\feedbackExport.csv", exportDir), csv.ToArray());
        }

        private void button2_Click(object sender, EventArgs e)
        {
            activeReport.AddNote();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if(emailForm == null || emailForm.IsDisposed)
            {
                emailForm = new Form2();
            }
            emailForm.ShowDialog();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (checkBox1.Checked)
            {
                ExportCSV();
            }
            //Generate the windows email command
            string receipients = String.Join(",", activeEmailList.GetRecipients());
            string subject = "Image Feedback";
            string body = GenerateEmailBody();
            string mailProcess = String.Format("mailto:{0}?subject={1}&body={2}", receipients, subject, body);

            

            //Use windows shell to execute a windows email command
            Process.Start(new ProcessStartInfo(mailProcess) { UseShellExecute = true });
        }

        private void button5_Click(object sender, EventArgs e)
        {
            activeReport.HideReport();
            currentReportIndex--;

            activeReport = reportList[currentReportIndex];
            activeReport.ShowReport();
            textBox1.Text = activeReport.GetImagePath();

            if(currentReportIndex == MIN_REPORT_INDEX)
            {
                button5.Enabled = false;
            }
            button6.Enabled = true;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            activeReport.HideReport();
            currentReportIndex++;

            activeReport = reportList[currentReportIndex];
            activeReport.ShowReport();
            textBox1.Text = activeReport.GetImagePath();

            if (currentReportIndex == MAX_REPORT_INDEX)
            {
                button6.Enabled = false;
            }
            button5.Enabled = true;
        }
    }
}