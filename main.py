from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import psycopg2
import pyodbc

# Đặt token của bot và thông tin cơ sở dữ liệu ở đây
DB_HOST = "HSVFPTDB07"
DB_NAME = "LSReport"
DB_USER = "dd"
DB_PASSWORD = "Hoahuongduong2908"
driver = '{ODBC Driver 17 for SQL Server}'

# Chuỗi kết nối SQL Server
connection_string = f'DRIVER={driver};SERVER={"HSVFPTDB07"};DATABASE={"LSReport"};UID={"dd"};PWD={"Hoahuongduong2908"}'

# Tạo kết nối SQL Server
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Đặt token của bot ở đây
TOKEN = "6652425688:AAFCp_sHXQilYE1pNvNZjpj84Yy5V_LnXmQ"

def start(update, context):
    user_id = update.message.from_user.id
    update.message.reply_text(user_id)

def save_to_database(update, context):
    
    user_id = update.message.from_user.id
    if (user_id==716505864 ) :
        msvn = 886092
    if (user_id==5305171584 ) :
        msvn = 960503
    # Lưu thông tin vào cơ sở dữ liệu
    #cursor.execute("SELECT 1")
    cursor.execute(f"INSERT INTO [WiseEyeOn39].[dbo].[CheckInOut] VALUES ({msvn}, DATEADD(MILLISECOND, -DATEPART(MILLISECOND, getdate()),getdate()),convert(datetime,convert(date,getdate())),'O' ,NULL ,'FP' ,'74' ,'255' )")
    conn.commit()

    update.message.reply_text(f"{msvn} done")
def handle_message(update, context):
    if update.message.text.strip().lower() == "fp":
    # Gọi hàm save_to_database khi nhận bất kỳ tin nhắn nào
        save_to_database(update, context)

def main():
    # Khởi tạo updater với token của bot
    updater = Updater(TOKEN, use_context=True)

    # Lấy dispatcher để đăng ký các xử lý sự kiện
    dp = updater.dispatcher

    # Đăng ký các xử lý sự kiện
    dp.add_handler(CommandHandler("cc", start)) 
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dp.add_handler(CommandHandler("fp", save_to_database))
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, save_to_database))

    # Bắt đầu chạy bot
    updater.start_polling()

    # Chạy bot cho đến khi bạn nhấn Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()