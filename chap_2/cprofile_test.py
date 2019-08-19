"""Profile the palingrams code"""
import cProfile
import palingrams

cProfile.run('palingrams.find_palingrams()')
