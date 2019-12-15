import downloadCleaner as dlClean
import emailTrasher as trasher 

def main():
    trasher.cleanInbox()
    dlClean.moveFilesToDesktop("C:/Users/noahe/Downloads")


if __name__ == "__main__":
    main()