#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>
#include <string.h>


void usage(){
   printf("Usage: connector [OPTIONS] \n");
   printf("    -b = [Required] Ip of the bastion host\n");
   printf("    -d = [Required] Ip of the destination\n");
   printf("    -k = [Required] Path to the private key\n");
   printf("    -u = [Required] User name\n");
   printf("    -j = [Optional] Jupyter-Notebook port 8888 forward to localhost\n");
   printf("    -r = [Optional] Rstudio-server port 8787 forward to localhost\n");
   printf("    -s = [Optional] Only shell access\n");
   printf("    -f = [Optional] SFTP port (22) forward to localhost\n");
   exit(EXIT_FAILURE);
}


void command_error(int int_error){
   if(int_error == 1){
      printf("ERROR: You have selected MULTIPLE connection types\n");
      printf("       Please select ONE of the followings\n");
      printf("           -j = [Optional] Jupyter-Notebook port (8888) forward to localhost\n");
      printf("           -r = [Optional] Rstudio-server port (8787) forward to localhost\n");
      printf("           -s = [Optional] Connect to the instance without any port forwarding\n");
      printf("           -f = [Optional] SFTP port (22) forward to localhost\n");
      exit(EXIT_FAILURE);
   }else if(int_error == 0){
      printf("ERROR: You have NOT selected a connection type\n");
      printf("       Please select ONE of the followings\n");
      printf("           -j = [Optional] Jupyter-Notebook port (8888) forward to localhost\n");
      printf("           -r = [Optional] Rstudio-server port (8787) forward to localhost\n");
      printf("           -s = [Optional] Connect to the instance without any port forwarding\n");
      printf("           -f = [Optional] SFTP port (22) forward to localhost\n");
      exit(EXIT_FAILURE);
   }else{
      printf("Unknown Error\n");
      abort();
   }
}


int main(int argc, char *argv[]){
   int opt;
   char *jump = NULL;
   char *destination = NULL;
   char *key = NULL;
   int jupyter = 0;
   char *remote_hostname = NULL;
   int rstudio = 0;
   int shell = 0;
   int ftp_connection = 0;

   char bastion_host[16] = "";
   char target_host[16] = "";
   char key_path[256] = "";
   char user_name[16] = "";

   char sudo[1024] = "ssh -i ";
   char space[] = " ";
   char map_jupyter[] = " -L 8888:localhost:8888 ";
   char map_rstudio[] = " -L 8787:localhost:8787 ";
   char at[] = "@";
   char proxy[] = " -o \"proxycommand ssh -W %h:\%p -i ";
   char ftp_map[] = " -L 22:localhost:22 ";


   while((opt=getopt(argc, argv, "b:d:k:u:rjsf")) != -1){
      switch(opt){
         case 'b':
            jump = optarg;
            strcat(bastion_host, jump);
            break;
         case 'd':
            destination = optarg;
            strcat(target_host, destination);
            break;
         case 'k':
            key = optarg;
            strcat(key_path, key);
            break;
         case 'u':
            remote_hostname = optarg;
            strcat(user_name, remote_hostname);
            break;
         case 'j':
            jupyter = 1;
            break;
         case 'r':
            rstudio = 1;
            break;
         case 's':
            shell = 1;
            break;
         case 'f':
            ftp_connection = 1;
            break;
         default:
            abort();
      }
   }


   if(argc > 1 && jump != NULL && destination != NULL && key != NULL && remote_hostname != NULL){
      
      if(jupyter == 1 && rstudio == 1 && shell == 1 && ftp_connection == 1){
         command_error(1);
      }else if(jupyter == 0 && rstudio == 0 && shell == 0 && ftp_connection == 0){
         command_error(0);
      }else if(jupyter == 1 && rstudio == 0 && shell == 0 && ftp_connection == 0){
         printf("############################################################################\n");
         printf("#      Activating: Jupyter-Notebook port 8888 forwarding to local host     #\n");
         printf("#      After the connection activate jupyter-notebook                      #\n");
         printf("#      Use: http://localhost:8888 to access Jupyter-Notebook               #\n");
         printf("############################################################################\n\n\n");
         sleep(3);
         strcat(sudo, key_path);
         strcat(sudo, map_jupyter);
         strcat(sudo, user_name);
         strcat(sudo, at);
         strcat(sudo, target_host);
         strcat(sudo, proxy);
         strcat(sudo, key_path);
         strcat(sudo , map_jupyter);
         strcat(sudo, user_name);
         strcat(sudo, at);
         strcat(sudo, bastion_host);
         strcat(sudo, "\"");
         // printf("%s\n", sudo);
         system(sudo);

      }else if(jupyter == 0 && rstudio == 1 && shell == 0 && ftp_connection == 0){
         printf("############################################################################\n");
         printf("#      Activating: Rstudio server port 8787 forwarding to local host       #\n");
         printf("#      Use: http://localhost:8787 to access Rstudio                        #\n");
         printf("############################################################################\n\n\n");
         sleep(3);
         strcat(sudo, key_path);
         strcat(sudo, map_rstudio);
         strcat(sudo, user_name);
         strcat(sudo, at);
         strcat(sudo, target_host);
         strcat(sudo, proxy);
         strcat(sudo, key_path);
         strcat(sudo , map_rstudio);
         strcat(sudo, user_name);
         strcat(sudo, at);
         strcat(sudo, bastion_host);
         strcat(sudo, "\"");
         // printf("%s\n", sudo);
         system(sudo);

      }else if(jupyter == 0 && rstudio == 0 && shell == 1 && ftp_connection == 0){
         printf("############################################################################\n");
         printf("#      Activating: Shell connection WITH OUT port forwarding               #\n");
         printf("############################################################################\n\n\n");
         sleep(3);
         strcat(sudo, key_path);
         strcat(sudo, space);
         strcat(sudo, user_name);
         strcat(sudo, at);
         strcat(sudo, target_host);
         strcat(sudo, proxy);
         strcat(sudo, key_path);
         strcat(sudo, space);
         strcat(sudo, user_name);
         strcat(sudo, at);
         strcat(sudo, bastion_host);
         strcat(sudo, "\"");
         // printf("%s\n", sudo);
         system(sudo);

      }else if(jupyter == 0 && rstudio == 0 && shell == 0 && ftp_connection == 1){
         printf("############################################################################################\n");
         printf("#      Activating: SFTP Forwarding port 22 to localhost                                    #\n");
         printf("#      Use: localhost as the destination and port 22 as the port on your SFTP client       #\n");
         printf("############################################################################################\n\n\n");
         sleep(3);
         strcat(sudo, key_path);
         strcat(sudo, ftp_map);
         strcat(sudo, user_name);
         strcat(sudo, at);
         strcat(sudo, target_host);
         strcat(sudo, proxy);
         strcat(sudo, key_path);
         strcat(sudo , ftp_map);
         strcat(sudo, user_name);
         strcat(sudo, at);
         strcat(sudo, bastion_host);
         strcat(sudo, "\"");
         // printf("%s\n", sudo);
         system(sudo);

      }else{
         command_error(1);
         
      }


   }else{
      usage();
   }

}