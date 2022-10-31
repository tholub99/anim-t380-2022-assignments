using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PipelineMidterm
{
    
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            string title = comboBox1.SelectedItem.ToString();
            Form1.activeEmailList = new EmailList(Form1.availableEmailLists[title]);
            FormatListView();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            Refresh();
        }

        private void Refresh(object sender, EventArgs e)
        {
            List<string> keyList = Form1.availableEmailLists.Keys.ToList();
            int activeIndex = keyList.IndexOf(Form1.activeEmailList.GetTitle());
            comboBox1.DataSource = keyList;
            comboBox1.SelectedIndex = activeIndex;
            FormatListView();
        }

        private void FormatListView()
        {
            listView1.Clear();
            listView1.View = View.Details;
            listView1.Columns.Add("Name", 140, HorizontalAlignment.Left);
            listView1.Columns.Add("Email", 160, HorizontalAlignment.Right);
            Dictionary<string, string> activeMap = Form1.activeEmailList.GetEmailMap();
            foreach (string name in activeMap.Keys)
            {
                string email = activeMap[name];
                string[] arr = new string[2];
                arr[0] = name;
                arr[1] = email;
                ListViewItem itm = new ListViewItem(arr);
                listView1.Items.Add(itm);
            }
        }
        //Add new name to list
        private void button1_Click(object sender, EventArgs e)
        {
            Form3 addForm = new Form3();
            addForm.ShowDialog();
        }

        //Remove name from list
        private void button2_Click(object sender, EventArgs e)
        {
            string nameToRemove = null;
            foreach(ListViewItem item in listView1.Items)
            {
                if(item.Selected)
                {
                    listView1.Items.Remove(item);
                    nameToRemove = item.Text;
                    break;
                }
            }
            if(nameToRemove != null)
            {
                Form1.activeEmailList.RemoveEmail(nameToRemove);
                FormatListView();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Dispose();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Form4 saveForm = new Form4();
            saveForm.ShowDialog();
        }
    }
}
