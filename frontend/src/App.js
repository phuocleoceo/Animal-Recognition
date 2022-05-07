import { ColorModeSwitcher } from './ColorModeSwitcher';
import React, { useState } from 'react';
import
{
  ChakraProvider, Box, Grid, theme, Text,
  Container, Button, Image, VStack, HStack
} from '@chakra-ui/react';
import { ViewIcon, LinkIcon } from "@chakra-ui/icons"

function App()
{
  const [recognition, setRecognition] = useState({
    animal: "Mèo",
    confidence: 100
  });

  const [image, setImage] = useState("./cat.jpg");
  const [selectedImage, setSelectedImage] = useState();

  const handleFileSelected = (e) =>
  {
    e.preventDefault();
    setSelectedImage(e.target.files[0]);
    setImage(URL.createObjectURL(e.target.files[0]));
  };

  const handleRecognition = () =>
  {

  }

  return (
    <ChakraProvider theme={theme}>
      <Box textAlign="center" fontSize="xl">
        <Grid minH="100vh" p={3}>
          <ColorModeSwitcher justifySelf="flex-end" />
          <Container>
            <VStack spacing={4}>
              <Image
                boxSize='60%'
                objectFit='cover'
                src={image}
                alt='Animal'
                fallbackSrc='https://via.placeholder.com/160'
              />

              <HStack>
                <Button colorScheme='teal' variant='outline'
                  leftIcon={<ViewIcon />} onClick={handleRecognition}>
                  Nhận diện
                </Button>

                <input accept="image/*" type="file" style={{ display: 'none' }}
                  id="contained-button-file" onChange={handleFileSelected} multiple />
                <label htmlFor="contained-button-file">
                  <Button as={"span"} colorScheme='teal'
                    variant='outline' leftIcon={<LinkIcon />}
                    style={{ cursor: 'pointer' }}>
                    Chọn ảnh
                  </Button>
                </label>
              </HStack>

              <VStack>
                <Text>Kết quả : {recognition.animal}</Text>
                <Text>Độ tin cậy : {recognition.confidence} (%)</Text>
              </VStack>
            </VStack>
          </Container>
        </Grid>
      </Box>
    </ChakraProvider >
  );
}

export default App;
