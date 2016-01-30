## Read excel -- 32bit R
read_excel = function(excel_file, sheet = "Sheet1"){
  require(RODBC)
  conn = odbcConnectExcel2007(excel_file) # open a connection to the Excel file
  sqlTables(conn)$TABLE_NAME # show all sheets
  df = sqlFetch(conn, "Sheet1") # read a sheet
  # df = sqlQuery(conn, "select * from [Sheet1 $]") # read a sheet (alternative SQL sintax)
  close(conn) # close the connection to the file
  return(df)
}

## Connection via odbc
read_odbc = function(query){
  t_start = proc.time()
  library(RODBC)
  myconn = odbcConnect("test") ## Both 32 and 64-bit have been setup.
  qr = readChar(query,nchar = 50000)
  df = as.data.frame(sqlQuery(myconn, qr,errors = FALSE), 
                     stringsAsFactors = FALSE)
  t_end = proc.time()
  print ( t_end - t_start)
  return(df)
}
read_odbc_char = function(qr){
  t_start = proc.time()
  library(RODBC)
  myconn = odbcConnect("test") ## Both 32 and 64-bit have been setup.
#   qr = readChar(query,nchar = 50000)
  df = as.data.frame(sqlQuery(myconn, qr,errors = FALSE), 
                     stringsAsFactors = FALSE)
  t_end = proc.time()
  print ( t_end - t_start)
  return(df)
}


query_odbc = function(query){
  t_start = proc.time()
  library(RODBC)
  myconn = odbcConnect("test") ## Both 32 and 64-bit have been setup.
  qr = query
  df = as.data.frame(sqlQuery(myconn, qr,errors = FALSE), 
                     stringsAsFactors = FALSE)
  t_end = proc.time()
  print ( t_end - t_start)
  return(df)
}

# df = read_odbc('classification.sql')                

## Connection via odbc
read_redshift = function(query_file){
  source('connect_db.r')
  query = readChar(query_file,nchar = 50000)
  df = dbGetQuery(testdb, 
                  query )
  return(df)
}

# condb = function(query_file,connect = 'odbc'){
#   if (connect == 'odbc'){
#     df = odbc(query_file)
#   }
#   if (connect == 'jdbc'){
#     df = read_redshift(query_file)
#   }
# }

pkgTest <- function(x)
{
  # x = as.character(substitute(x)))
  if (!require(x,character.only = TRUE))
  {
    install.packages(x,dep=TRUE)
    if(!require(x,character.only = TRUE)) stop("Package not found")
  }
}
pkgTest("MASS")

## Separate a column of strings into two columns of strings.

## sort multiple columns
sort_data = function(data, sortnames ){
#   data<-data.frame(a=rnorm(10),b=rnorm(10)) 
#   data<-data.frame(a=rnorm(10),b=rnorm(10),c=rnorm(10))
#   sortnames <- c("a", "b")
  sorted = data[do.call("order", data[sortnames]), ]
  return(sorted)
}
# aa = rules_df[1:20,]
#  aa[,"indicator_ind"] =as.numeric(aa[,"indicator_ind"])

## separate columns
# do.call(rbind, strsplit(as.vector(df[,1]),split = "-")) 

## common numb in a list
# Reduce(intersect, ind_lst)
