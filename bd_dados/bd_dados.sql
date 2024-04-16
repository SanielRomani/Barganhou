using System.Data.OleDb;

string connStr = @"Provider=Microsoft.Jet.OLEDB.4.0;Data Source=C:\Users\sanielcr1\OneDrive - Votorantim\bd-smadm.accdb;";
OleDbConnection conn = new OleDbConnection(connStr);
conn.Open();

string sql = "SELECT [bd-cadastro].[Código], [bd-cadastro].[Nome], [bd-cadastro].[Email], [bd-cadastro].[Matricula] FROM [bd-cadastro]";
OleDbCommand cmd = new OleDbCommand(sql, conn);

OleDbDataReader reader = cmd.ExecuteReader();
while (reader.Read())
{
    Response.Write(reader[0].ToString());
}

reader.Close();
conn.Close();
