FROM  node:20

WORKDIR /app


COPY . .


#install all depedencies
RUN npm install 

EXPOSE 5173

#To run the app 
CMD ["npm", "run", "dev", "--", "--host"]

