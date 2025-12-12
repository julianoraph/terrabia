import React from 'react'
import { Link } from 'react-router-dom'
import {
  Box,
  Container,
  Typography,
  Button,
  Grid,
  Card,
  CardContent,
  CardActions,
  useTheme,
  useMediaQuery,
  Divider,
  Chip,
  Stack
} from '@mui/material'
import {
  Grass,
  LocalGroceryStore,
  LocalShipping,
  Security,
  TrendingFlat,
  ArrowForward
} from '@mui/icons-material'
import { motion } from 'framer-motion'
import './Home.css'

const Home = () => {
  const theme = useTheme()
  const isMobile = useMediaQuery(theme.breakpoints.down('md'))

  // Brutalist color palette
  const brutalistColors = {
    primary: '#000000',
    secondary: '#FFFFFF',
    accent: '#FF6B6B',
    background: '#F8F9FA',
    surface: '#FFFFFF',
    border: '#000000'
  }

  const features = [
    {
      icon: <Grass sx={{ fontSize: 32, color: brutalistColors.accent }} />,
      title: 'PRODUITS FRAIS',
      description: 'Directement du champ à votre table',
      stat: '24h max'
    },
    {
      icon: <LocalGroceryStore sx={{ fontSize: 32, color: brutalistColors.accent }} />,
      title: 'ACHAT DIRECT',
      description: 'Supprimez les intermédiaires',
      stat: '-40% coûts'
    },
    {
      icon: <LocalShipping sx={{ fontSize: 32, color: brutalistColors.accent }} />,
      title: 'LIVRAISON EXPRESS',
      description: 'Dans toute la région',
      stat: '2h-6h'
    },
    {
      icon: <Security sx={{ fontSize: 32, color: brutalistColors.accent }} />,
      title: 'PAIEMENT SÉCURISÉ',
      description: 'Cryptée et transparente',
      stat: '100% sûr'
    }
  ]

  return (
    <div className="brutalist-home">
      {/* Navigation Bar */}
      <motion.nav 
        initial={{ y: -100 }}
        animate={{ y: 0 }}
        className="brutalist-nav"
        style={{
          backgroundColor: brutalistColors.secondary,
          borderBottom: `3px solid ${brutalistColors.primary}`,
          position: 'sticky',
          top: 0,
          zIndex: 1000
        }}
      >
        <Container maxWidth="lg">
          <Box sx={{ 
            display: 'flex', 
            justifyContent: 'space-between', 
            alignItems: 'center',
            py: 2
          }}>
            <Typography 
              variant="h5" 
              component={Link} 
              to="/"
              sx={{ 
                textDecoration: 'none',
                color: brutalistColors.primary,
                fontWeight: 900,
                letterSpacing: '-1px'
              }}
            >
              TERRABIA
            </Typography>
            
            <Stack direction="row" spacing={3}>
              <Button 
                component={Link} 
                to="/products"
                sx={{ 
                  color: brutalistColors.primary,
                  fontWeight: 700,
                  '&:hover': { backgroundColor: brutalistColors.background }
                }}
              >
                PRODUITS
              </Button>
              <Button 
                variant="contained"
                component={Link}
                to="/register"
                sx={{ 
                  backgroundColor: brutalistColors.primary,
                  color: brutalistColors.secondary,
                  borderRadius: 0,
                  fontWeight: 700,
                  px: 3,
                  '&:hover': { backgroundColor: brutalistColors.accent }
                }}
              >
                REJOINDRE
              </Button>
            </Stack>
          </Box>
        </Container>
      </motion.nav>

      {/* Hero Section - Asymmetrical Layout */}
      <section className="brutalist-hero">
        <Container maxWidth="lg">
          <Grid container spacing={6} alignItems="center">
            <Grid item xs={12} md={7}>
              <motion.div
                initial={{ opacity: 0, x: -50 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.8 }}
              >
                <Chip 
                  label="NOUVEAU" 
                  sx={{ 
                    backgroundColor: brutalistColors.accent,
                    color: brutalistColors.secondary,
                    fontWeight: 700,
                    mb: 3,
                    borderRadius: 0
                  }}
                />
                
                <Typography 
                  variant={isMobile ? "h2" : "h1"} 
                  component="h1"
                  sx={{
                    fontWeight: 900,
                    lineHeight: 1.1,
                    mb: 3,
                    letterSpacing: '-2px',
                    color: brutalistColors.primary
                  }}
                >
                  LE MARCHÉ
                  <br />
                  <Box component="span" sx={{ color: brutalistColors.accent }}>
                    AGRICOLE
                  </Box>
                  <br />
                  SANS FILTRES
                </Typography>

                <Typography 
                  variant="h6" 
                  sx={{ 
                    mb: 4,
                    fontWeight: 400,
                    maxWidth: '90%',
                    color: brutalistColors.primary
                  }}
                >
                  Une plateforme brute, directe et transparente qui connecte les agriculteurs du Cameroun aux consommateurs du monde entier. Pas de marketing, juste des produits.
                </Typography>

                <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap' }}>
                  <Button
                    variant="contained"
                    size="large"
                    component={Link}
                    to="/products"
                    endIcon={<ArrowForward />}
                    sx={{
                      backgroundColor: brutalistColors.primary,
                      color: brutalistColors.secondary,
                      borderRadius: 0,
                      py: 1.5,
                      px: 4,
                      fontWeight: 700,
                      '&:hover': {
                        backgroundColor: brutalistColors.accent
                      }
                    }}
                  >
                    EXPLORER LES PRODUITS
                  </Button>
                  
                  <Button
                    variant="outlined"
                    size="large"
                    component={Link}
                    to="/register"
                    sx={{
                      borderColor: brutalistColors.primary,
                      color: brutalistColors.primary,
                      borderRadius: 0,
                      py: 1.5,
                      px: 4,
                      fontWeight: 700,
                      '&:hover': {
                        borderColor: brutalistColors.accent,
                        color: brutalistColors.accent
                      }
                    }}
                  >
                    CRÉER UN COMPTE
                  </Button>
                </Box>
              </motion.div>
            </Grid>

            <Grid item xs={12} md={5}>
              <motion.div
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.6, delay: 0.2 }}
                style={{
                  backgroundColor: brutalistColors.accent,
                  padding: '2rem',
                  border: `3px solid ${brutalistColors.primary}`,
                  position: 'relative',
                  marginTop: isMobile ? '2rem' : '-4rem'
                }}
              >
                <Typography variant="h5" sx={{ fontWeight: 700, mb: 2, color: brutalistColors.secondary }}>
                  CHIFFRES CLÉS
                </Typography>
                
                <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 2 }}>
                  {[
                    { label: 'Agriculteurs', value: '500+' },
                    { label: 'Produits', value: '2K+' },
                    { label: 'Livraisons/jour', value: '1.5K' },
                    { label: 'Satisfaction', value: '98%' }
                  ].map((item, index) => (
                    <Box key={index} sx={{ textAlign: 'center' }}>
                      <Typography variant="h4" sx={{ fontWeight: 900, color: brutalistColors.secondary }}>
                        {item.value}
                      </Typography>
                      <Typography variant="body2" sx={{ color: brutalistColors.secondary }}>
                        {item.label}
                      </Typography>
                    </Box>
                  ))}
                </Box>
              </motion.div>
            </Grid>
          </Grid>
        </Container>
      </section>

      {/* Features Section - Grid Layout */}
      <section className="brutalist-features" style={{ backgroundColor: brutalistColors.background, padding: '6rem 0' }}>
        <Container maxWidth="lg">
          <Typography 
            variant="h3" 
            component="h2" 
            sx={{ 
              fontWeight: 900, 
              mb: 6, 
              textAlign: 'center',
              color: brutalistColors.primary
            }}
          >
            POURQUOI TERRABIA ?
          </Typography>

          <Grid container spacing={4}>
            {features.map((feature, index) => (
              <Grid item xs={12} sm={6} md={3} key={index}>
                <motion.div
                  initial={{ opacity: 0, y: 30 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                >
                  <Card 
                    sx={{ 
                      backgroundColor: brutalistColors.surface,
                      border: `2px solid ${brutalistColors.border}`,
                      borderRadius: 0,
                      height: '100%',
                      transition: 'transform 0.2s',
                      '&:hover': {
                        transform: 'translateY(-4px)',
                        borderColor: brutalistColors.accent
                      }
                    }}
                  >
                    <CardContent sx={{ p: 3 }}>
                      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 2 }}>
                        {feature.icon}
                        <Chip 
                          label={feature.stat}
                          size="small"
                          sx={{ 
                            backgroundColor: brutalistColors.primary,
                            color: brutalistColors.secondary,
                            fontWeight: 700,
                            borderRadius: 0
                          }}
                        />
                      </Box>
                      
                      <Typography 
                        variant="h6" 
                        component="h3" 
                        sx={{ 
                          fontWeight: 700, 
                          mb: 1,
                          color: brutalistColors.primary
                        }}
                      >
                        {feature.title}
                      </Typography>
                      
                      <Typography variant="body2" sx={{ color: brutalistColors.primary }}>
                        {feature.description}
                      </Typography>
                    </CardContent>
                    
                    <CardActions sx={{ p: 3, pt: 0 }}>
                      <Button 
                        endIcon={<TrendingFlat />}
                        sx={{ 
                          color: brutalistColors.accent,
                          fontWeight: 700,
                          p: 0,
                          '&:hover': { backgroundColor: 'transparent' }
                        }}
                      >
                        En savoir plus
                      </Button>
                    </CardActions>
                  </Card>
                </motion.div>
              </Grid>
            ))}
          </Grid>
        </Container>
      </section>

      {/* CTA Section - Full Width */}
      <motion.section
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        className="brutalist-cta"
        style={{
          backgroundColor: brutalistColors.primary,
          color: brutalistColors.secondary,
          padding: '6rem 0'
        }}
      >
        <Container maxWidth="md">
          <Typography 
            variant="h3" 
            component="h2" 
            sx={{ 
              fontWeight: 900, 
              mb: 3,
              textAlign: 'center'
            }}
          >
            REJOIGNEZ LA RÉVOLUTION
          </Typography>
          
          <Typography 
            variant="h6" 
            sx={{ 
              mb: 5, 
              textAlign: 'center',
              opacity: 0.9
            }}
          >
            Que vous cultiviez la terre ou que vous cherchiez des produits authentiques, 
            TERRABIA vous connecte sans intermédiaires.
          </Typography>

          <Box sx={{ 
            display: 'flex', 
            gap: 3, 
            justifyContent: 'center',
            flexWrap: isMobile ? 'wrap' : 'nowrap'
          }}>
            <Button
              variant="contained"
              size="large"
              component={Link}
              to="/register?type=farmer"
              sx={{
                backgroundColor: brutalistColors.accent,
                color: brutalistColors.secondary,
                borderRadius: 0,
                py: 2,
                px: 5,
                fontWeight: 700,
                minWidth: '200px',
                '&:hover': {
                  backgroundColor: brutalistColors.secondary,
                  color: brutalistColors.primary
                }
              }}
            >
              JE SUIS AGRICULTEUR
            </Button>
            
            <Button
              variant="outlined"
              size="large"
              component={Link}
              to="/register?type=customer"
              sx={{
                borderColor: brutalistColors.secondary,
                color: brutalistColors.secondary,
                borderRadius: 0,
                py: 2,
                px: 5,
                fontWeight: 700,
                minWidth: '200px',
                '&:hover': {
                  backgroundColor: brutalistColors.secondary,
                  color: brutalistColors.primary
                }
              }}
            >
              JE SUIS CLIENT
            </Button>
          </Box>
        </Container>
      </motion.section>

      {/* Footer */}
      <footer className="brutalist-footer" style={{ backgroundColor: brutalistColors.background, padding: '3rem 0' }}>
        <Container maxWidth="lg">
          <Divider sx={{ borderColor: brutalistColors.border, mb: 4 }} />
          
          <Grid container spacing={4}>
            <Grid item xs={12} md={6}>
              <Typography variant="h6" sx={{ fontWeight: 700, mb: 2, color: brutalistColors.primary }}>
                TERRABIA
              </Typography>
              <Typography variant="body2" sx={{ color: brutalistColors.primary, maxWidth: '400px' }}>
                Plateforme agricole directe. Connectant les agriculteurs camerounais aux consommateurs mondiaux depuis 2023.
              </Typography>
            </Grid>
            
            <Grid item xs={6} md={3}>
              <Typography variant="subtitle2" sx={{ fontWeight: 700, mb: 2, color: brutalistColors.primary }}>
                NAVIGATION
              </Typography>
              <Stack spacing={1}>
                <Button 
                  component={Link} 
                  to="/products"
                  sx={{ 
                    justifyContent: 'flex-start',
                    color: brutalistColors.primary,
                    p: 0,
                    '&:hover': { color: brutalistColors.accent }
                  }}
                >
                  Produits
                </Button>
                <Button 
                  component={Link} 
                  to="/register"
                  sx={{ 
                    justifyContent: 'flex-start',
                    color: brutalistColors.primary,
                    p: 0,
                    '&:hover': { color: brutalistColors.accent }
                  }}
                >
                  Inscription
                </Button>
              </Stack>
            </Grid>
            
            <Grid item xs={6} md={3}>
              <Typography variant="subtitle2" sx={{ fontWeight: 700, mb: 2, color: brutalistColors.primary }}>
                CONTACT
              </Typography>
              <Typography variant="body2" sx={{ color: brutalistColors.primary }}>
                contact@terrabia.cm
                <br />
                +237 XXX XXX XXX
              </Typography>
            </Grid>
          </Grid>
          
          <Typography variant="caption" sx={{ display: 'block', mt: 4, color: brutalistColors.primary }}>
            © 2023 TERRABIA. Tous droits réservés.
          </Typography>
        </Container>
      </footer>
    </div>
  )
}

export default Home