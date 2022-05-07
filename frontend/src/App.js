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
                src='./cat.jpg'
                alt='Animal'
                fallbackSrc='https://via.placeholder.com/160'
              />

              <HStack>
                <Button colorScheme='teal' variant='outline' leftIcon={<ViewIcon />}>
                  Nhận diện
                </Button>

                <Button colorScheme='teal' variant='outline' leftIcon={<LinkIcon />}>
                  Chọn ảnh
                </Button>
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
