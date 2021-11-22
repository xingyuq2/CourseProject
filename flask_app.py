from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from recommender import recommend
from utils import read_from_csv


app = Flask(__name__)
CORS(app)

OK = 200
BAD_REQUEST = 400
NOT_FOUND = 404


# http://127.0.0.1:5000/api/video?id={attr_value}
@app.route('/api/video', methods=['GET'])
def get_video_by_id():
    """
    Get the video detail by id.
    """
    # get id
    video_id = request.args.get('id')
    response = {}
    if not video_id:
        # id not found in request
        response['BAD_REQUEST'] = 'id input not found'
        return make_response(jsonify(response), BAD_REQUEST)

    # search for id in csv file
    list_of_video_dict = read_from_csv()
    for curr_dict in list_of_video_dict:
        if curr_dict['id'] == video_id:
            # found id, return with status 200
            return make_response(jsonify(curr_dict), OK)
    
    # id not found in csv, return with status 404
    response['NOT_FOUND'] = 'id given not found in csv file'
    return make_response(jsonify(response), NOT_FOUND)


# http://127.0.0.1:5000/api/all
@app.route('/api/all', methods=['GET'])
def get_all_video():
    """
    Get the all video
    """
    response = {}
    list_of_video_dict = read_from_csv()
    if not list_of_video_dict:
        response['NOT_FOUND'] = 'nothing in csv file'
        return make_response(jsonify(response), NOT_FOUND)
    
    return make_response(jsonify(list_of_video_dict), OK)


# http://127.0.0.1:5000/api/recommendations?id={attr_value}
@app.route('/api/recommendations', methods=['GET'])
def get_video_recommendatinos_by_id():
    """
    Get the video recommendations by id.
    """
    video_id = request.args.get('id')
    response = {}
    if not video_id:
        response['BAD_REQUEST'] = 'id input not found'
        return make_response(jsonify(response), BAD_REQUEST)

    # get list of index of recommended videos
    list_of_index = []
    list_of_video_dict = read_from_csv()
    for idx, curr_dict in enumerate(list_of_video_dict):
        if curr_dict['id'] == video_id:
            list_of_index = recommend(idx)
    
    # get list of recommended videos by index and return
    if list_of_index:
        list_recommended_video_dict = []
        for curr_idx in list_of_index:
            list_recommended_video_dict.append(list_of_video_dict[curr_idx])
        return make_response(jsonify(list_recommended_video_dict), OK)
            
    response['NOT_FOUND'] = 'id given not found in csv file'
    return make_response(jsonify(response), NOT_FOUND)
    

if __name__ == '__main__':
    app.run(debug=True)
